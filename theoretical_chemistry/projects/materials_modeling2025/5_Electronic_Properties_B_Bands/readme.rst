=============================================
TASK 5: Electronic properties: B (Bands, ASE)
=============================================

In this task, we'll  automate band structure calculation using ASE. The workflow consists of a SCF calculation, followed by a NSCF (bands) calculation (set via calculation = 'bands' in &CONTROL, with matching outdir/ prefix to read the SCF charge density, similar to DOS calculation); then post-processing with bands.x and plotband.x. plotband.x is optional (since bands.x generated bands.dat.gnu can be plotted directly e.g., with Grace), but it automatically marks the high-symmetry points and Fermi level in the final image. While ASE automates the execution sequence, each post-processing tool requires specific inputs similar to DOS calculations.

Step 5.1:
Start with the final_relaxed_structure.vasp (from Task 3, ASE) and use seekpath (either online, (https://seekpath.materialscloud.io/ or locally installed) to symmetrize the structure and generate a high-symmetry k-point path through the Brillouin zone.

Step 5.2:
Visualize the path and note the high-symmetry points (In this example: Γ—X—U|K—Γ—L—W—X), then copy the symmetrized cell (under Quantum ESPRESSO pw.x input) into the ASE script electronic_properties_b_si.py.

Step 5.3:
Copy the seekpath generated list of k-point path into a sperate file (kp), and convert it to ASE format using:
awk '{printf("    [%s, %s, %s, %s],\n", $1, $2, $3, $4)}' kp > kp_parsed
and then copy the parsed k points into the script (seekpath generated k points can be used in manual QE runs, but ASE format is slightly different).

Step 5.4:
python3 electronic_properties_b_si.py > electronic_properties_b_si.out
(update the Quantum ESPRESSO executable path to your local pw.x location.)


python electronic_properties_b_si.py > electronic_properties_b_si_py.logfile


Inspect electronic_b_si.out to verify all steps have completed successfully., then review the bands and plotband input/output files. Finally, compare your computed band structure with silicon’s experimental results.

Note: NSCF (bands) calculation does not print Fermi level, so Fermi level has to be taken from the preceding SCF step. In the job script, ASE automatically handles it.
Note: Install ghostscript (check the accompanied notes), if you want the script to convert the plotband.x generated postscript file to jpg, other wise disable the relevant line.
