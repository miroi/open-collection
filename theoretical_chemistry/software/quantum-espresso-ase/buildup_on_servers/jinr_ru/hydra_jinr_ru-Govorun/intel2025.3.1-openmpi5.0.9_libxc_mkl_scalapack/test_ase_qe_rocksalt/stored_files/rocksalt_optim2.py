#
# https://wiki.fysik.dtu.dk/ase/tutorials/lattice_constant.html#using-the-stress-tensor
#
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import LBFGS
from ase.constraints import StrainFilter

rocksalt = bulk('NaCl', crystalstructure='rocksalt', a=6)

# Pseudopotentials from SSSP Efficiency v1.3.0
#pseudopotentials = {'Na': 'na_pbe_v1.5.uspp.F.UPF', 'Cl': 'cl_pbe_v1.4.uspp.F.UPF'}
local_pseudopotentials = {'Na': 'Na.upf', 'Cl': 'Cl.upf'}

# Optionally create profile to override paths in ASE configuration:
QEprofile = EspressoProfile(
    command='mpiexec -np 2 /usr/bin/pw.x', 
    pseudo_dir='./',
)

input_data = {
    'system': {'ecutwfc': 48, 'ecutrho': 480},
    'disk_io': 'low',  # Automatically put into the 'control' section
}

calc = Espresso(
    profile=QEprofile,
    pseudopotentials=local_pseudopotentials,
    tstress=True,  # deprecated, put in input_data
    tprnfor=True,  # deprecated, put in input_data
    input_data=input_data,
    kpts=(5,5,5),
    )

rocksalt.calc = calc

print("single point calc: ")
rocksalt.get_potential_energy()  # This will run a single point calculation


print("ase lattice geometry optimization, with stress tensor: ")
sf = StrainFilter(rocksalt)
opt = LBFGS(sf)
opt.run(fmax=0.005)  # This will run a geometry optimization using ASE's LBFGS algorithm

print("ase geometry optimization, with LBFGS:")
opt = LBFGS(rocksalt)
opt.run(fmax=0.005)  # This will run a geometry optimization using ASE's LBFGS algorithm

# Print lattice constant...
print("Obtained optimized lattice constant, a")
print((8 * rocksalt.get_volume() / len(rocksalt)) ** (1.0 / 3.0))
