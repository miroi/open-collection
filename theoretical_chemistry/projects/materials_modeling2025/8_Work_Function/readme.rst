===========================
TASK 8: Work function (ASE)
===========================

The work function is defined as the minimum energy required to extract an electron from a solid to a point immediately outside its surface. It is not a bulk material property but rather a surface-specific characteristic that we will calculate for our graphene slab example. the work flow consists of first performing an SCF calculation, then using pp.x to extract the electrostatic potential (plot number 11), followed by planar and macroscopic averaging along the vacuum direction with average.x, from which the finnally the work function can be estimated. As usual, we will use ASE to automate the execution sequence.

Step 8.1:
python3 potential.py > potential.out
(update the Quantum ESPRESSO executable path to your local pw.x location.)

Inspect the potential.out file, and the individual SCF, pp.x, and average.x input and output files to ensure proper execution. Then plot the potential profile from potential_results/avg.dat alongside the Fermi level obtained from the SCF calculation. The vacuum level is identified as the flat region of the electrostatic potential outside the slab surface, then compute the work function as Work Function = Vacuum Level - Fermi Level. Finally compare your obtained values with standard reported values of graphene.

Note:
The 'assume_isolated': '2D' setting introduces artificial image charges that distort the electrostatic potential at the cell boundaries (notice the unphysical peaks at the start and end of your plot), though it is necessary to maintain accuracy of forces and energies, especially for asymmetric slabs requiring dipole correction. Now remove this flag, rerun the example, and inspect the resulting potential profile to observe a more physically meaningful potential profile.
