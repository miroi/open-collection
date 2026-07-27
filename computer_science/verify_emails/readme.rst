======================
Verify email addresses
======================

GoogleAI Python script for verifycation of vcf file emails.

pip install email-validator dnspython

example of usage
----------------
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/computer_science/verify_emails/.python verify_emails.py emails.vcf --workers 20 --txt-report audit.txt --
clean-vcf filtered.vcf
Found 1525 contacts with 1525 unique emails.
Starting verification across 20 threads...
Progress: Completed 100/1525 email lookups.
Progress: Completed 200/1525 email lookups.
Progress: Completed 300/1525 email lookups.
Progress: Completed 400/1525 email lookups.
Progress: Completed 500/1525 email lookups.
Progress: Completed 600/1525 email lookups.
Progress: Completed 700/1525 email lookups.
Progress: Completed 800/1525 email lookups.
Progress: Completed 900/1525 email lookups.
Progress: Completed 1000/1525 email lookups.
Progress: Completed 1100/1525 email lookups.
Progress: Completed 1200/1525 email lookups.
Progress: Completed 1300/1525 email lookups.
Progress: Completed 1400/1525 email lookups.
Progress: Completed 1500/1525 email lookups.
Progress: Completed 1525/1525 email lookups.

Txt report successfully saved to: audit.txt
Cleaned VCF successfully generated at: **filtered.vcf**
 -> Kept **1504** out of 1525 total contacts.


