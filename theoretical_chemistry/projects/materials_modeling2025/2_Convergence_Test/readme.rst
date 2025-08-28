TASK 2: Automated Cutoff and K-points Convergence Test (ASE)
------------------------------------------------------------

In convergence testing, we systematically increase two key parameters separately (not simultaneously): (1) Plane-wave cutoff energy (ecutwfc) (2) K-points grid density (K_POINTS). The goal is to find the point where the total energy stabilizes (saturates) with respect to further changes in these parameters. It can be done manually by running multiple SCF calculations (as in TASK 1) and comparing energies at each step. However the current task uses a ASE python script (convergence_test_si.py) to automate the process. All necessary parameters are already pre-configured in the script, including: (1) QE SCF input parameters (2) Atomic structure of silicon (3) Convergence test logic. Only one modification is required: Replace the QE executable path with your local pw.x location in the script.

The convergence script uses three parameters to automate testing:
(1) ecutwfc_values = np.arange(20, 120, 5) Tests cutoffs from 20 to 120 Ry in steps of 5 Ry.
(2) kpoints_values = [(k,k,k) for k in range(2, 25)]  Tests k-grids from (2×2×2) to (25×25×25)
(3) energy_tol = 0.01 # Sets the convergence threshold (0.01 meV/atom). The script stops when energy changes between steps are smaller than this tolerance.

Adjust ranges (e.g., np.arange(20, 80, 10)), and higher tolerance (e.g. 0.05) for quicker testing.

Step 2.1: Run the ASE job
--------------------------

python3 convergence_test_si.py > convergence_test_si.out

python convergence_test_si.py > convergence_test_si.logfile

Another pseudopotential
~~~~~~~~~~~~~~~~~~~~~~~
python convergence_test2_si.py > convergence_test2_si.logfile

Note: When performing a series of calculations, ASE automatically overwrites the Quantum ESPRESSO output (.pwo) and input (.pwi) files after each step. How many different SCF calculations did ASE run to converge cutoff energy / K-points grid in this task?


TASK 2.2 
~~~~~~~~~
Run a final QE SCF calculation with your converged ecutwfc and kpoints (similar to TASK 1), along with tstress = .true. and tprnfor = .true. in the input file (under &CONTROL) to compute stress and atomic forces and inspect the output.
/path/to/qe/bin/pw.x < Si_force_stress.in > Si_force_stress.out


mpirun -np 8 /usr/bin/pw.x < Si_force_stress.in > Si_force_stress.logfile




