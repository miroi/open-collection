#!/usr/bin/env python3
#
#  Cohesive energy calculation for fcc aluminum with query to openkim.org for lattice constant
#
"""
Compute the cohesive energy and pressure of an FCC Al crystal using the
Ercolessi-Adams EAM potential implemented as a Portable Model (PM) in
OpenKIM for the equilibrium lattice constant obtained by querying openkim.org.
"""

from ase.calculators.kim import KIM
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import GPa
from kim_query import get_lattice_constant_cubic

model = "EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005"

# Perform query to get lattice constant for this model
print("doing query to get lattice constant for this model=",model)
a0 = get_lattice_constant_cubic([model], ["fcc"], ["Al"], ["angstrom"])[0]
print("obtained a0=",a0)

# Set up crystal and calculator
atoms = FaceCenteredCubic("Al", latticeconstant=a0)
calc = KIM(model)
atoms.set_calculator(calc)

# Compute energy/pressure
ecoh = -atoms.get_potential_energy() / len(atoms)
stress = atoms.get_stress()
pressure_MPa = (-sum(stress[:3]) / 3.0) * 1e3 / GPa

print("Computed cohesive energy of {:.3f} eV/atom (experiment: 3.39 eV/atom)".format(ecoh))
print("Computed pressure of {} MPa".format(pressure_MPa))

