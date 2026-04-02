from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator
from chgnet.model import StructOptimizer
from chgnet.model.model import CHGNet
from pymatgen.core import Structure, Molecule
from ase.io import read
from pymatgen.io.ase import AseAtomsAdaptor
import pubchempy as pcp


# 1. nitrobenzene ...
atoms_ase = read('nitrobenzene.sdf')

# write out
for atom in atoms_ase:
    print(f"Index {atom.index}: {atom.symbol}  Position: {atom.position}")

# 2. Load the pretrained CHGNet model
# By default, this loads the latest version (e.g., v0.3.0)
model = CHGNet.load()

# 3. Attach the CHGNet Calculator to the atoms object
#atoms.calc = CHGNetCalculator(model)

# Load as a Molecule instead of a Structure
molecule = Molecule.from_file('nitrobenzene.sdf')
print("Molecule.from_file :",molecule)

##CHGNet can optimize non-periodic molecules. To do so, you must convert the molecule into a boxed Structure with a large amount of vacuum 
# box) to satisfy the model's requirement for a periodic lattice.
# 2. Convert to a Structure by adding a large lattice (e.g., 20x20x20 Angstroms)

structure = molecule.get_boxed_structure(20, 20, 20)


relaxer = StructOptimizer()
result = relaxer.relax(structure,fmax=0.05)

# 5. Extract the optimized molecule
print("CHGNet relaxed structure: \n", result["final_structure"])


relaxed_struct = result["final_structure"]

relaxed_mol = Molecule.from_sites(relaxed_struct.sites)

relaxed_mol = relaxed_mol.get_centered_molecule()

print("relaxed_mol:\n",relaxed_mol)

relaxed_mol.to(filename="nitrobenzene_optimized.sdf")

print("relaxed total energy in eV:", result['trajectory'].energies[-1])


# BFGS is a common choice for molecular geometry optimization
# 'trajectory' saves the optimization steps for later visualization
#dyn = BFGS(atoms, trajectory='nitrobenzene_opt.traj', logfile='opt.log')

# 5. Run the optimization
# fmax defines the convergence criteria (force < 0.05 eV/Å)
#dyn.run(fmax=0.05)

#print(f"Optimization complete. Final energy: {atoms.get_potential_energy():.4f} eV")
#print(f"Final positions:\n{atoms.get_positions()}")

