=======================================
TASK 7: Surfaces and 2D materials (ASE)
=======================================


This task focuses on analyzing the electronic properties of surfaces and 2D materials, using graphene as an example. Begin by inspecting the graphite structure, select two atoms with identical z-coordinates, and then manually increase the c lattice parameter to a large arbitrary value (e.g., 15 Å) while adjusting the z-coordinates of the selected two atoms to half that value (e.g., 7.5 Å) to create a well-separated, single-layer graphene structure. After visualizing this new structure, copy the TASK 2 convergence test script and edit it: (1) update it with the graphene structure and carbon pseudopotential (2) 2D material specific changes: 'assume_isolated': '2D' (3) change the k-points grid from cubic to a 2D grid divisible by three (e.g., 3k, 3k, 1) to ensure proper sampling of the Dirac point at (1/3, 1/3, 0). For a 2D material, electronic dispersion is flat in the z-direction, so only one k-point is needed to sample it accurately.

Step 7.1:
Run the convergence test
python3 convergence_test_graphene.py > convergence_test_graphene.out

Step 7.2
Copy the TASK 3: Cell relaxation script to the working directory and update it for graphene by moving from a full, unconstrained relaxation to a constrained one. This means using a mask in the UnitCellFilter—a boolean list [xx, yy, zz, yz, xz, xy]—to only relax the in-plane lattice vectors (xx, yy) while keeping the out-of-plane vector (zz) and all cell angles (yz, xz, xy) fixed. This is the equivalent of setting up a constrained relaxation with QE's in-built cell_dofree tag (xy or 2Dxy).
Then run the relaxation:
python3 cell_relaxation_graphene.py > cell_relaxation_graphene.out

Step 7.3
Copy the TASK 4: Electronic properties: A script, and update it with the relaxed graphene structure and all other relevant parameters. Then run the calculation:
python3 electronic_properties_graphene.py > electronic_properties_graphene.out

Inspect all the obtained results similar to the previous analysis, and then examine the calculated projected DOS for a carbon atom's p orbitals. This file contains five columns where the first two were already covered in TASK 4; columns 3-5 describes the orbital projections onto pz, px, and py oribtals (in that specific order. For the exact orbital orderings for different cases (e.g. spin-orbit, spin polarized etc.), consult the PROJWFC manual. Plot the contributions from pz, px, and py. The expected nature for graphene is that near the Fermi level, the electronic states are formed primarily by the out-of-plane pz orbitals, which create the characteristic Dirac cones. Determine if your results show this same behavior. Now plot the same for Si p orbital, what differences do you see? Why?
