from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import LBFGS

rocksalt = bulk('NaCl', crystalstructure='rocksalt', a=6.0)

# Pseudopotentials from SSSP Efficiency v1.3.0
pseudopotentials = {'Na': 'na_pbe_v1.5.uspp.F.UPF', 'Cl': 'cl_pbe_v1.4.uspp.F.UPF'}

# Optionally create profile to override paths in ASE configuration:
#profile = EspressoProfile(
#    command='/path/to/pw.x', pseudo_dir='/path/to/pseudopotentials'
#)

#calc = Espresso(profile=profile, pseudopotentials=pseudopotentials)
calc = Espresso(pseudopotentials=pseudopotentials)

rocksalt.calc = calc

rocksalt.get_potential_energy()  # This will run a single point calculation

opt = LBFGS(rocksalt)

opt.run(fmax=0.005)  # This will run a geometry optimization using ASE's LBFGS algorithm

# Print lattice constant...
print((8 * rocksalt.get_volume() / len(rocksalt)) ** (1.0 / 3.0))
