#!/bin/bash

set -e

echo "=============================================="
echo "Starting DOXol-M2 equilibration: 6.1 -> 6.6"
echo "=============================================="

# -----------------------------
# Step 6.1
# -----------------------------

echo
echo "=============================================="
echo "Preparing step6.1_equilibration"
echo "=============================================="

gmx grompp \
-f step6.1_equilibration.mdp \
-c step6.0_minimization.gro \
-r step6.0_minimization.gro \
-p topol.top \
-n index_eq.ndx \
-o step6.1_equilibration.tpr

echo
echo "Running step6.1_equilibration..."

gmx mdrun \
-deffnm step6.1_equilibration

echo
echo "Checking step6.1_equilibration.log..."

# Confirm the run actually finished
if ! grep -q "Finished mdrun" step6.1_equilibration.log
then
    echo "ERROR: step6.1 did not reach 'Finished mdrun'."
    exit 1
fi

# Search only for real problem messages
if grep -Eiq \
"Fatal error|LINCS WARNING|segmentation fault|nan detected" \
step6.1_equilibration.log
then
    echo "ERROR: Real problem detected in step6.1_equilibration.log"
    exit 1
fi

echo "Step 6.1 completed successfully."


# -----------------------------
# Steps 6.2 -> 6.6
# -----------------------------

for i in 2 3 4 5 6
do

    prev=$((i-1))

    echo
    echo "=============================================="
    echo "Preparing step6.${i}_equilibration"
    echo "Previous stage = step6.${prev}_equilibration"
    echo "=============================================="

    gmx grompp \
    -f step6.${i}_equilibration.mdp \
    -c step6.${prev}_equilibration.gro \
    -r step6.0_minimization.gro \
    -t step6.${prev}_equilibration.cpt \
    -p topol.top \
    -n index_eq.ndx \
    -o step6.${i}_equilibration.tpr

    echo
    echo "Running step6.${i}_equilibration..."

    gmx mdrun \
    -deffnm step6.${i}_equilibration

    echo
    echo "Checking step6.${i}_equilibration.log..."

    # Confirm normal completion
    if ! grep -q "Finished mdrun" step6.${i}_equilibration.log
    then
        echo "ERROR: step6.${i} did not reach 'Finished mdrun'."
        exit 1
    fi

    # Detect only real failures
    if grep -Eiq \
    "Fatal error|LINCS WARNING|segmentation fault|nan detected" \
    step6.${i}_equilibration.log
    then
        echo "ERROR: Real problem detected in step6.${i}_equilibration.log"
        exit 1
    fi

    echo "Step 6.${i} completed successfully."

done


echo
echo "=============================================="
echo "DOXol-M2 equilibration completed successfully"
echo "Final structure:"
echo "step6.6_equilibration.gro"
echo "Final checkpoint:"
echo "step6.6_equilibration.cpt"
echo "=============================================="
