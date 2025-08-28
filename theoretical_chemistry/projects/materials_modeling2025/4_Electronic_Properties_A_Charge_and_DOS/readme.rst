TASK 4: Electronic properties: A (Charge and DOS, ASE)
======================================================

In this task, we'll calculate a few key electronic properties — (1) 3D charge density (using post-processing tool pp.x), (2) Löwdin partial charges (using projwfc.x), (3) total DOS (using dos.x), and (4) projected DOS (using projwfc.x) — through a streamlined ASE workflow combining SCF and NSCF calculations. The SCF calculation generates the charge density and Löwdin charges, while a subsequent NSCF calculation (with calculation='nscf' in the CONTROL namelist and matching outdir/prefix to read the SCF charge density) produces the DOS data using a denser k-grid. Each post-processing tool requires its specific input format (detailed in accompanying notes), but ASE automates the execution sequence.

First, copy your relaxed atomic structure into the provided ASE script (electronic_a_si.py) and update the Quantum ESPRESSO executable path to your local pw.x location.

Step 4.1:
---------
python3 electronic_properties_a_si.py > electronic_properties_a_si.out

Inspect electronic_a_si.out to verify all steps have completed successfully. Also inspect the individual pp, dos and projwfc input and output files.
Open the generated charge_density.cube file in VESTA to visualize the 3D electron density. For the total density of states (TDOS), plot the first two columns (E (eV) and dos(E)) from total_dos.dat using any plotting tool (e.g., Grace, matplotlib), then shift the x-axis by subtracting the Fermi energy (found in the QE output, grep Fermi *.pwo) to align the Fermi energy to 0 eV (in Grace: Data > Transformation > Evaluate Expression: x=x-<Fermi Energy>). Repeat this process for the projected DOS (PDOS) by plotting the first two columns from the first Si atom's s and p orbital files, again offsetting by Fermi energy. Finally, examine lowdin.out and check the computed Löwdin partial charges for each Si atom.
Compare your computed DOS with silicon's experimental band gap- does your match? Why? Why not?

Note: To verify the quality of the projections, two key checks are necessary: (1) ensure the spilling parameter is low enough, and (2) confirm that the summed PDOS (from .pdos_tot) closely matches the total DOS, at least below the Fermi level. While the script automatically reports both metrics, it's strongly recommended to manually plot and compare the .pdos_tot and total_dos.dat files and visually validate it.

Note: SCF (Self-Consistent Field) calculations iteratively solve the Kohn-Sham equations to find the ground-state electron density and total energy by converging the charge density. NSCF (Non-Self-Consistent Field) calculations use the pre-converged charge density from SCF but compute eigenvalues on a denser k-point grid without re-converging the density. For DOS (Density of States), NSCF is essential because it provides higher-resolution sampling of the Brillouin zone, capturing fine electronic structure details that the coarser SCF grid would miss, while avoiding the computational cost of fully re-converging at each k-point. This ensures accurate and smooth DOS plots without redundant SCF iterations.

python electronic_properties_a_si.py >  electronic_properties_a_si_py.logfile


