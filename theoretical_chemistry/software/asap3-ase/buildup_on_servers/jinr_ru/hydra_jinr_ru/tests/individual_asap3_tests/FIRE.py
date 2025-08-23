"""Test local crystal structure analysis (CNA and Coordination number)."""

from asap3 import EMT
from asap3.testtools import ReportTest
from ase.optimize import FIRE
from ase.build import bulk
import numpy as np

atoms = bulk('Cu')
atoms = atoms.repeat((7, 7, 100))

print("Testing FIRE relaxation")
atoms.calc = EMT()
e0 = atoms.get_potential_energy()
natoms = atoms.get_global_number_of_atoms()
ReportTest("Number of atoms", natoms, 4900, 0)
print("Potential energy before perturbation:", e0, e0/natoms)

dx = 0.1 * np.sin(42 * np.arange(3 * len(atoms)))
dx.shape = (-1, 3)
atoms.set_positions(dx + atoms.get_positions())
e1 = atoms.get_potential_energy()
print("Potential energy after perturbation:", e1, e1/natoms)

dyn = FIRE(atoms)
dyn.run(0.01)
e2 = atoms.get_potential_energy()
print("Potential energy after perturbation:", e2, e2/natoms)
ReportTest("Energy after relaxation", e2, e0, 0.02)
ReportTest("Number of FIRE steps", dyn.nsteps, 61, 5)


ReportTest.Summary()
