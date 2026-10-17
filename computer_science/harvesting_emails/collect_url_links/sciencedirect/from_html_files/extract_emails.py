import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Regex pattern for matching email addresses
EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)


def extract_emails_from_html(file_path):
    """Extract all unique email addresses from an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"  [ERROR] Could not read {file_path}: {e}")
        return set()

    emails = set()
    for match in EMAIL_PATTERN.finditer(content):
        email = match.group(0).rstrip('.,;:')
        emails.add(email.lower())
    return emails


def escape_vcf_value(value):
    """Escape special characters for VCF format."""
    return (
        value.replace('\\', '\\\\')
             .replace(';', '\\;')
             .replace(',', '\\,')
             .replace('\n', '\\n')
    )


def write_vcf(filepath, email_records):
    """
    Write a single VCF file containing all emails.

    email_records: dict of email -> set of source filenames
    """
    lines = [
        'BEGIN:VCARD',
        'VERSION:3.0',
    ]
    # Single vCard with all emails; using the first email as display name
    # is optional. Instead we'll create one vCard per email but in one file.

    vcards = []
    for email in sorted(email_records.keys()):
        sources = ', '.join(sorted(email_records[email]))
        local_part = email.split('@')[0]
        # Use the local part as a friendly display name (title-cased, cleaned)
        display_name = local_part.replace('.', ' ').replace('_', ' ').replace('-', ' ').title()

        vcard = [
            'BEGIN:VCARD',
            'VERSION:3.0',
            f'N:{escape_vcf_value(display_name)};;;;',
            f'FN:{escape_vcf_value(display_name)}',
            f'EMAIL;TYPE=INTERNET:{email}',
            f'NOTE:Found in: {escape_vcf_value(sources)}',
            'END:VCARD',
        ]
        vcards.append('\r\n'.join(vcard))

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write('\r\n'.join(vcards) + '\r\n')

    print(f"\n[✓] Wrote {len(vcards)} contact(s) to '{filepath}'")


def main(folder='.'):
    folder_path = Path(folder)
    if not folder_path.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        return

    html_files = sorted(
        list(folder_path.glob('*.html')) + list(folder_path.glob('*.htm'))
    )

    if not html_files:
        print(f"No HTML files found in '{folder_path.resolve()}'.")
        return

    print(f"Found {len(html_files)} HTML file(s) in '{folder_path.resolve()}'\n")

    all_emails = set()
    email_sources = {}  # email -> set of filenames
    summary = {}

    for html_file in html_files:
        emails = extract_emails_from_html(html_file)
        summary[html_file.name] = emails
        all_emails.update(emails)

        for email in emails:
            email_sources.setdefault(email, set()).add(html_file.name)

        print(f"=== {html_file.name} ===")
        if emails:
            for email in sorted(emails):
                print(f"  {email}")
        else:
            print("  (no emails found)")
        print()

    print("=" * 60)
    print(f"TOTAL UNIQUE EMAILS FOUND: {len(all_emails)}")
    print("=" * 60)
    for email in sorted(all_emails):
        print(f"  {email}")

    # Write single VCF file
    if all_emails:
        vcf_path = folder_path / 'extracted_emails.vcf'
        write_vcf(vcf_path, email_sources)
    else:
        print("\n[i] No emails found; VCF file not created.")

    return summary


if __name__ == '__main__':
    folder = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(folder)
