from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

rocksalt = bulk('NaCl', crystalstructure='rocksalt', a=6.0)

print("unptimized rocksalt lattice constant a=",(8 * rocksalt.get_volume() / len(rocksalt)) ** (1.0 / 3.0))

# Pseudopotentials from SSSP Efficiency v1.3.0
local_pseudopotentials = {'Na':'na_pbe_v1.5.uspp.F.UPF', 'Cl':'cl_pbe_v1.4.uspp.F.UPF'}

# Optionally create profile to override paths in ASE configuration:
#profile = EspressoProfile(
#    command='/path/to/pw.x', pseudo_dir='/path/to/pseudopotentials'
#)
#profile = EspressoProfile( pseudo_dir='./')

NaCl_input_data = { 
    'calculation': 'scf', 'tprnfor': True, 'tstress': True,
    'system': {'ecutwfc': 40, 'ecutrho': 320},
    'disk_io': 'low',  # Automatically put into the 'control' section
}

ecf = FrechetCellFilter(rocksalt)

#calc = Espresso(profile=profile, pseudopotentials=pseudo_dir)
##calc = Espresso(pseudopotentials=pseudopotentials)
calc = Espresso(pseudopotentials=local_pseudopotentials, input_data=NaCl_input_data,)

rocksalt.calc = calc
#ecf.calc = calc

#rocksalt.get_potential_energy()  # This will run a single point calculation
ecf.get_potential_energy()  # This will run a single point calculation

#opt = LBFGS(rocksalt)
opt = LBFGS(ecf)

#opt.run(fmax=0.005)  # This will run a geometry optimization using ASE's LBFGS algorithm
opt.run(fmax=0.02)  # This will run a geometry optimization using ASE's LBFGS algorithm

# Print lattice constant...
print("QE optimized rocksalt lattice constant a=",(8 * rocksalt.get_volume() / len(rocksalt)) ** (1.0 / 3.0))
