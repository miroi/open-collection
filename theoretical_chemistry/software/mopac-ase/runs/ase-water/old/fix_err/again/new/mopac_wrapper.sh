#!/usr/bin/expect -f
# Expect script to handle MOPAC's interactive prompt
set timeout 30
set mopac_path "/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac"
set label [lindex $argv 0]

# Remove .mop extension if present
set label [string map {".mop" ""} $label]

# Start MOPAC
spawn $mopac_path $label

# Wait for the prompt and send Enter
expect "Press (return) to continue"
send "\r"

# Wait for job to complete
expect eof

# Check if output file was created
if {[file exists "${label}.out"]} {
    exit 0
} else {
    exit 1
}
