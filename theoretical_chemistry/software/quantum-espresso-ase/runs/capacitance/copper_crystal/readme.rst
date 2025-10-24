===========
Cu crystal
===========

Cu.upf from https://www.pseudo-dojo.org/

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/capacitance/copper_crystal/.python Cu.py


Running SCF calculation...
  Total energy: -20637.937209 eV

[Phase A.] Extracting charge density and Löwdin charges from SCF calculation...

1. Calculating charge density from SCF...
  pp.x completed successfully

2. Running projwfc.x on SCF...
  projwfc.x completed successfully

3. Extracting Löwdin charges from SCF (projwfc.out)...
  Löwdin charges saved to lowdin.out
  Spilling parameter value: 0.008300
  Excellent (<0.05)

Cleaning up SCF files and preparing for NSCF calculation...
  Moved all SCF-related files to scf_files directory

Running NSCF calculation for DOS with k-grid (16, 16, 16)...
  NSCF completed, wavefunctions generated for DOS

[Phase B.] Calculating DOS and PDOS from NSCF calculation...

4. Calculating TDOS from NSCF...
  dos.x completed successfully

5. Calculating PDOS from NSCF...
  projwfc.x completed successfully

6. Organizing PDOS files from NSCF...
  PDOS files moved to pdos_results directory

7. Verifying TDOS vs summed PDOS (ONLY below Fermi level)...
  Fermi level from NSCF calculation: 17.5322 eV
  Verification failed: module 'numpy' has no attribute 'trapezoid'

[Phase C.] Calculating Quantum Capacitance per Unit Cell...
  Fermi level: 17.5322 eV
  DOS at E_F: 1.147000 states/eV/cell
  Quantum Capacitance per unit cell: 1.8377e-19 F/cell
  Results saved to quantum_capacitance.dat

=== Electronic Structure Analysis Complete ===
Generated files:
- Charge density (from SCF): charge_density.cube
- Löwdin Charges (from SCF): lowdin.out
- Total DOS (from NSCF): total_dos.dat
- PDOS files (from NSCF): pdos_results/
- Quantum capacitance data saved to quantum_capacitance.dat


