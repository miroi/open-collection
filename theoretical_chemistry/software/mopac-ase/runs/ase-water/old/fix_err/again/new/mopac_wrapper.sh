#!/bin/bash
# Simple wrapper that handles MOPAC's interactive prompt
MOPAC_PATH="/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac"

# Get the input file (ASE passes it as argument)
INPUT_FILE="$1"
BASE_NAME="${INPUT_FILE%.mop}"

# Try multiple methods to send Enter key
# Method 1: echo with pipe
echo "" | $MOPAC_PATH $BASE_NAME 2>/dev/null

# Method 2: If method 1 failed, try with printf
if [ ! -f "${BASE_NAME}.out" ]; then
    printf "\n" | $MOPAC_PATH $BASE_NAME 2>/dev/null
fi

# Method 3: If still failed, try with yes
if [ ! -f "${BASE_NAME}.out" ]; then
    yes "" | head -n 1 | $MOPAC_PATH $BASE_NAME 2>/dev/null
fi

# Method 4: Try with cat and here-document
if [ ! -f "${BASE_NAME}.out" ]; then
    cat <<< "" | $MOPAC_PATH $BASE_NAME 2>/dev/null
fi

exit 0
