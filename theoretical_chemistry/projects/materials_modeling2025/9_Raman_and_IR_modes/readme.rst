TASK 9: Raman Spectroscopy (ASE)
================================

Raman spectroscopy measures the inelastic scattering of light by phonons to characterize vibrational modes in materials. This workflow calculates the Raman spectrum of bulk silicon using Density Functional Perturbation Theory (DFPT), beginning with an SCF ground state calculation, followed by a DFPT phonon calculation at the Gamma point to obtain vibrational frequencies and Raman intensities, and concluding with dynmat.x to process and output the Raman-active modes. As with the previous tasks, ASE automates the entire execution sequence.

Step 9.1:
python3 raman_si.py > raman_si.out
(Update the Quantum ESPRESSO executable paths to your local pw.x and ph.x locations.)

Inspect the raman_si.out file and examine the individual SCF, ph.x, and dynmat.x input and output files to verify proper execution. The dynmat.out output file will list the Raman and IR active modes. Compare these with experimentally reported values for bulk silicon.

Note:
This calculation needs LDA norm-conserving pseudopotentials (required for Raman property calculations).
