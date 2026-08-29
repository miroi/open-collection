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

def parse_vcf_blocks(vcf_path):
    """Parses VCF file into individual contact blocks and maps emails to their parent block."""
    contacts = []
    current_block = []
    current_emails = set()
    
    # Matches lines like EMAIL;TYPE=INTERNET:example@domain.com or EMAIL:test@test.com
    email_pattern = re.compile(r'^EMAIL(?:;[^:]*)?:(.*)$', re.IGNORECASE)
    
    try:
        with open(vcf_path, 'r', encoding='utf-8') as file:
            for line in file:
                current_block.append(line)
                if line.strip().upper() == "BEGIN:VCARD":
                    current_block = [line]
                    current_emails = set()
                elif line.strip().upper() == "END:VCARD":
                    contacts.append({
                        'block': current_block,
                        'emails': current_emails
                    })
                else:
                    match = email_pattern.match(line.strip())
                    if match:
                        email_address = match.group(1).strip()
                        if email_address:
                            current_emails.add(email_address)
    except FileNotFoundError:
        print(f"Error: The file '{vcf_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        exit(1)
        
    return contacts

def verify_email_dns(email):
    """Performs syntax validation and explicit MX record queries using public DNS."""
    try:
        validation = validate_email(email, check_deliverability=False)
        domain = validation.domain
        
        try:
            mx_records = custom_resolver.resolve(domain, 'MX')
            if mx_records:
                return email, "Valid", f"MX Records found ({len(mx_records)} hosts)"
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            try:
                custom_resolver.resolve(domain, 'A')
                return email, "Valid", "A record fallback"
            except Exception:
                return "Invalid", "No active MX or A records"
        except dns.exception.Timeout:
            return email, "Timeout", "DNS resolution lifetime expired"
                
    except EmailNotValidError as error:
        return email, "Invalid", str(error)
    except Exception as general_error:
        return email, "Unknown", f"Network Error: {str(general_error)}"

def process_vcf_verification(vcf_path, txt_output_path, clean_vcf_path, max_workers):
    """Orchestrates parallel verification, logs text reports, and generates a clean VCF."""
    contacts = parse_vcf_blocks(vcf_path)
    
    # Gather all unique emails across all contact entries
    all_emails = set()
    for contact in contacts:
        all_emails.update(contact['emails'])
        
    unique_emails = sorted(list(all_emails))
    
    if not unique_emails:
        print("No emails found to verify.")
        return

    print(f"Found {len(contacts)} contacts with {len(unique_emails)} unique emails.")
    print(f"Starting verification across {max_workers} threads...")
    
    # Core verification registry
    email_status_registry = {}
    valid_lines = []
    invalid_lines = []
    
    # 1. Execute concurrent DNS verification lookups
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(verify_email_dns, email): email for email in unique_emails}
        
        for i, future in enumerate(as_completed(futures), 1):
            email, status, details = future.result()
            email_status_registry[email] = status
            
            formatted_line = f"{email:<40} | {status:<8} | {details}"
            if status == "Valid":
                valid_lines.append(formatted_line)
            else:
                invalid_lines.append(formatted_line)
                
            if i % 100 == 0 or i == len(unique_emails):
                print(f"Progress: Completed {i}/{len(unique_emails)} email lookups.")

    # 2. Generate the segregated text report
    try:
        with open(txt_output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 90 + "\n")
            f.write(f" EMAIL VERIFICATION REPORT - Total Audited: {len(unique_emails)}\n")
            f.write("=" * 90 + "\n\n")
            
            f.write(f"### VALID EMAIL ADDRESSES ({len(valid_lines)}) ###\n")
            f.write(f"{'Email Address':<40} | {'Status':<8} | {'Verification Details'}\n")
            f.write("-" * 90 + "\n")
            f.write("\n".join(sorted(valid_lines)) + "\n\n\n")
            
            f.write("=" * 90 + "\n")
            f.write(f"### INVALID / FAILED EMAIL ADDRESSES ({len(invalid_lines)}) ###\n")
            f.write(f"{'Email Address':<40} | {'Status':<8} | {'Verification Details'}\n")
            f.write("-" * 90 + "\n")
            f.write("\n".join(sorted(invalid_lines)) + "\n")
        print(f"\nTxt report successfully saved to: {txt_output_path}")
    except Exception as e:
        print(f"Error saving txt report: {str(e)}")

    # 3. Generate the cleaned VCF file
    clean_contact_count = 0
    try:
        with open(clean_vcf_path, 'w', encoding='utf-8') as f_vcf:
            for contact in contacts:
                # If a contact has no email, keep it, or if it has emails, ensure at least one is Valid
                if not contact['emails'] or any(email_status_registry.get(e) == "Valid" for e in contact['emails']):
                    f_vcf.writelines(contact['block'])
                    clean_contact_count += 1
        print(f"Cleaned VCF successfully generated at: **{clean_vcf_path}**")
        print(f" -> Kept **{clean_contact_count}** out of {len(contacts)} total contacts.")
    except Exception as e:
        print(f"Error saving cleaned VCF: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract, parallel-verify emails, and generate a sanitized VCF.")
    parser.add_argument("vcf_file", help="Path to the target input .vcf file")
    parser.add_argument(
        "--workers", 
        type=int, 
        default=30, 
        help="Number of concurrent worker threads (default: 30)"
    )
    parser.add_argument(
        "--txt-report", 
        default="verification_report.txt", 
        help="Path to save the text report (default: verification_report.txt)"
    )
    parser.add_argument(
        "--clean-vcf", 
        default="clean_contacts.vcf", 
        help="Path to save the clean VCF output (default: clean_contacts.vcf)"
    )
    
    args = parser.parse_args()
    process_vcf_verification(args.vcf_file, args.txt_report, args.clean_vcf, args.workers)

