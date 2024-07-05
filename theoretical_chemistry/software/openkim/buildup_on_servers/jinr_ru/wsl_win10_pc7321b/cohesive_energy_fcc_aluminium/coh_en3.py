#!/usr/bin/env python3

# Cohesive energy calculation for fcc aluminum (loop over all Al potentials in openkim.org)

"""
Compute the cohesive energy of an FCC Al crystal using all interatomic potentials for Al archived in openkim.org.
"""
from ase.calculators.kim import KIM
from kim_query import get_lattice_constant_cubic, get_available_models
from ase.lattice.cubic import FaceCenteredCubic

print("{:11s}  {}".format("Ecoh [eV]  ", "KIM Potential"))

# Query openkim.org to get list of all interatomic potentials for Al
models = get_available_models(species=["Al"], potential_type=["any"])

# Loop over all potentials
for model in models:

    try:
        # Setup calculator
        calc = KIM(model)

        # Perform query to get lattice constant for this model
        a0 = get_lattice_constant_cubic([model], ["fcc"], ["Al"], ["angstrom"])[0]

        # Build crystal and attach calculator
        atoms = FaceCenteredCubic("Al", latticeconstant=a0)
        atoms.calc = calc

        # Compute  and print energy
        ecoh = -atoms.get_potential_energy() / len(atoms)
        print("{:11.3f}  {}".format(ecoh, model))

        # Clear calculator
        calc.__del__()

    except:
        print("{:11s}  {}".format("unavailable", model))
