#!/bin/bash
# Wrapper script for MOPAC that handles interactive prompt
MOPAC_PATH="/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac"

# Get the input file (ASE passes it as argument)
INPUT_FILE="$1"
BASE_NAME="${INPUT_FILE%.mop}"

# Change to the directory where the input file is
cd "$(dirname "$INPUT_FILE")"

# Try multiple methods to send Enter key
# Method 1: Use echo with pipe (most common)
echo "" | $MOPAC_PATH $BASE_NAME 2>&1

# Method 2: If method 1 failed, try with printf
if [ ! -f "${BASE_NAME}.out" ]; then
    printf "\n" | $MOPAC_PATH $BASE_NAME 2>&1
fi

# Method 3: If still failed, try with yes
if [ ! -f "${BASE_NAME}.out" ]; then
    yes "" | head -n 1 | $MOPAC_PATH $BASE_NAME 2>&1
fi

# Method 4: Try with expect (if available)
if [ ! -f "${BASE_NAME}.out" ] && command -v expect &> /dev/null; then
    expect -c "
    spawn $MOPAC_PATH $BASE_NAME
    expect \"Press (return) to continue\"
    send \"\r\"
    expect eof
    " 2>&1
fi

# Exit with success if output file exists
if [ -f "${BASE_NAME}.out" ]; then
    exit 0
else
    exit 1
fi
