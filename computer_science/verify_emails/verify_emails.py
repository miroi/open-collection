import argparse
import re
import dns.resolver
from concurrent.futures import ThreadPoolExecutor, as_completed
from email_validator import validate_email, EmailNotValidError

# Configure a robust public DNS resolver to bypass WSL routing issues
custom_resolver = dns.resolver.Resolver(configure=False)
custom_resolver.nameservers = ['8.8.8.8', '1.1.1.1', '8.8.4.4']
custom_resolver.timeout = 2.0       
custom_resolver.lifetime = 4.0      

def extract_emails_from_vcf(vcf_path):
    """Extracts unique raw email addresses specifically from EMAIL tags in a VCF file."""
    emails = set()
    email_pattern = re.compile(r'^EMAIL(?:;[^:]*)?:(.*)$', re.IGNORECASE)
    
    try:
        with open(vcf_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = email_pattern.match(line.strip())
                if match:
                    email_address = match.group(1).strip()
                    if email_address:
                        emails.add(email_address)
    except FileNotFoundError:
        print(f"Error: The file '{vcf_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        exit(1)
    return emails

def verify_email_dns(email):
    """Performs syntax validation and explicit MX record queries using public DNS."""
    try:
        # 1. Syntax check via email-validator (bypassing its default dns check)
        validation = validate_email(email, check_deliverability=False)
        domain = validation.domain
        
        # 2. Explicit internet connection using public nameservers
        try:
            mx_records = custom_resolver.resolve(domain, 'MX')
            if mx_records:
                return email, "Valid", f"MX Records found ({len(mx_records)} hosts)"
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            try:
                custom_resolver.resolve(domain, 'A')
                return email, "Valid", "A record fallback"
            except Exception:
                return email, "Invalid", "No active MX or A records"
        except dns.exception.Timeout:
            return email, "Timeout", "DNS resolution lifetime expired"
                
    except EmailNotValidError as error:
        return email, "Invalid", str(error)
    except Exception as general_error:
        return email, "Unknown", f"Network Error: {str(general_error)}"

def process_vcf_verification(vcf_path, output_path, max_workers):
    """Orchestrates parallel network verification and saves segregated results to a txt file."""
    extracted_emails = sorted(list(extract_emails_from_vcf(vcf_path)))
    
    if not extracted_emails:
        print("No emails found to verify.")
        return

    print(f"Found {len(extracted_emails)} unique emails. Starting verification across {max_workers} threads...")
    
    valid_results = []
    invalid_results = []
    
    # Execute lookups concurrently across a pool of threads
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(verify_email_dns, email): email for email in extracted_emails}
        
        # Collect and separate results dynamically as they complete
        for i, future in enumerate(as_completed(futures), 1):
            email, status, details = future.result()
            formatted_line = f"{email:<40} | {status:<8} | {details}"
            
            if status == "Valid":
                valid_results.append(formatted_line)
            else:
                invalid_results.append(formatted_line)
                
            # Visual progress counter in console
            if i % 100 == 0 or i == len(extracted_emails):
                print(f"Progress: Completed {i}/{len(extracted_emails)} lookups.")

    # Write the sorted, separated findings into the output txt file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 90 + "\n")
            f.write(f" EMAIL VERIFICATION REPORT - Total Audited: {len(extracted_emails)}\n")
            f.write("=" * 90 + "\n\n")
            
            # Section 1: Valid Emails
            f.write(f"### VALID EMAIL ADDRESSES ({len(valid_results)}) ###\n")
            f.write(f"{'Email Address':<40} | {'Status':<8} | {'Verification Details'}\n")
            f.write("-" * 90 + "\n")
            if valid_results:
                f.write("\n".join(sorted(valid_results)) + "\n")
            else:
                f.write("[No valid emails found]\n")
                
            f.write("\n\n" + "=" * 90 + "\n")
            
            # Section 2: Invalid / Failed Emails (Separated cleanly at the bottom)
            f.write(f"### INVALID / FAILED EMAIL ADDRESSES ({len(invalid_results)}) ###\n")
            f.write(f"{'Email Address':<40} | {'Status':<8} | {'Verification Details'}\n")
            f.write("-" * 90 + "\n")
            if invalid_results:
                f.write("\n".join(sorted(invalid_results)) + "\n")
            else:
                f.write("[No invalid emails found - all clean!]\n")
                
        print(f"\nVerification complete! Results written out to: **{output_path}**")
        print(f" -> Valid entries: {len(valid_results)}")
        print(f" -> Invalid/Failed entries: {len(invalid_results)}")
        
    except Exception as e:
        print(f"Error saving output file: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and verify email addresses from a VCF file, saving separated output.")
    parser.add_argument("vcf_file", help="Path to the target .vcf file")
    parser.add_argument(
        "--output", 
        default="verification_report.txt", 
        help="Path to save the output text file (default: verification_report.txt)"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=25, 
        help="Number of concurrent worker threads (default: 25)"
    )
    
    args = parser.parse_args()
    process_vcf_verification(args.vcf_file, args.output, args.workers)

