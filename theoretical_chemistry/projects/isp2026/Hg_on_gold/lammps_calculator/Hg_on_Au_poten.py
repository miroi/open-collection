from ase import Atom, Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.lammpslib import LAMMPSlib
from ase.optimize import BFGS

# 1. Build the Au(111) slab (4 layers, 3x3 supercell)
slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)

# 2. Add the Hg adsorbate at a 'hollow' site
# Height of 2.5 A is a reasonable starting guess for optimization
add_adsorbate(slab, 'Hg', height=2.5, position='fcc')

# 3. Define LAMMPS Hybrid Potential Commands
# Type 1 = Au, Type 2 = Hg
# LJ parameters are estimates; replace with literature values if available
cmds = [
    "pair_style hybrid eam lj/cut 10.0",
    "pair_coeff 1 1 eam Au_u3.eam",           # Au-Au (EAM)
    "pair_coeff 2 2 lj/cut 0.05 3.0",        # Hg-Hg (LJ: epsilon, sigma)
    "pair_coeff 1 2 lj/cut 0.15 2.8",        # Au-Hg (LJ: cross-interaction)
]

# 1. SET ENVIRONMENT VARIABLES
# Replace '/usr/local/bin/lmp_serial' with the actual path to your LAMMPS binary
# You can find this path by typing 'which lmp_serial' or 'which lmp' in your terminal.
lmp_exe = '/usr/bin/lmp'
os.environ['ASE_LAMMPSRUN_COMMAND'] = lmp_exe
os.environ['LAMMPS_COMMAND'] = lmp_exe

# 2. DEFINE PATHS
# Use the full absolute path to your potential file
pot_file_path = '/usr/share/lammps/potentials/NiAlH_jea.eam.alloy'
pot_filename = os.path.basename(pot_file_path) # Extract 'NiAlH_jea.eam.alloy'


# 4. Initialize the Calculator
# 'specorder' maps ASE atom types to LAMMPS types 1 and 2
calc = LAMMPSlib(lmpcmds=cmds, 
                 specorder=['Au', 'Hg'], 
                 log_file='opt.log')

slab.calc = calc

# 5. Run the Optimization
opt = BFGS(slab, trajectory='hg_on_au.traj')
opt.run(fmax=0.05)

print(f"Final Potential Energy: {slab.get_potential_energy():.4f} eV")

