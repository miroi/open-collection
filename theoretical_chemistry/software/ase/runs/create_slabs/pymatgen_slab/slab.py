#
#  https://fhi-aims-club.gitlab.io/tutorials/slab-calculations-and-surface-simulations-with-fhi-aims/P1-Creating_Structures/#creating-surface-slabs-using-pymatgen
#
from pymatgen.core.surface import SlabGenerator, Lattice, Structure
from pymatgen.io.ase import AseAtomsAdaptor

# Create the diamond Si bulk first
lattice = Lattice.cubic(5.43)
Si = Structure(lattice, ["Si", "Si", "Si", "Si",
                         "Si", "Si", "Si", "Si"],
               [[0.00000, 0.00000, 0.50000],
                [0.75000, 0.75000, 0.75000],
                [0.00000, 0.50000, 0.00000],
                [0.75000, 0.25000, 0.25000],
                [0.50000, 0.00000, 0.00000],
                [0.25000, 0.75000, 0.25000],
                [0.50000, 0.50000, 0.50000],
                [0.25000, 0.25000, 0.75000]])

# Now we use the pymatgen SlabGenerator to create the Si(100) surface 
slabgen = SlabGenerator(Si, (1,0,0), min_slab_size=2, min_vacuum_size=6, in_unit_planes=True, center_slab=True)
Si_100 = slabgen.get_slabs()[0]

# Pymatgen doesn't support the aims input/output format yet
# We use ase to do the geometry output
ase_py = AseAtomsAdaptor()
ase_struc = ase_py.get_atoms(Si_100)

ase_struc.write("Si_100.in", scaled=True)
