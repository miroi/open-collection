
# https://www.ovito.org/manual/python/introduction/examples/batch_scripts/voronoi_indices.html

# Import OVITO modules.
from ovito.io import *
from ovito.modifiers import *

# Import NumPy module.
import numpy

# Load a simulation snapshot of a Cu-Zr metallic glass.
pipeline = import_file("input/simulation.0.dump")

# The LAMMPS dump file imported above contains only numeric atom type IDs but 
# no chemical element names or atom radius information. That's why we explicitly set the
# atomic radii of Cu & Zr atoms now (required for polydisperse Voronoi tessellation).
def assign_particle_radii(frame, data):
    atom_types = data.particles_.particle_types_
    atom_types.type_by_id_(1).radius = 1.35   # Cu atomic radius assigned to atom type 1
    atom_types.type_by_id_(2).radius = 1.55   # Zr atomic radius assigned to atom type 2
pipeline.modifiers.append(assign_particle_radii)

# Set up the Voronoi analysis modifier.
voro = VoronoiAnalysisModifier(
    compute_indices = True,
    use_radii = True,
    edge_threshold = 0.1
)
pipeline.modifiers.append(voro)

# Let OVITO compute the results.
data = pipeline.compute()

# Access computed Voronoi indices.
# This is an (N) x (M) array, where M is the maximum face order.
voro_indices = data.particles['Voronoi Index']

# This helper function takes a two-dimensional array and computes a frequency
# histogram of the data rows using some NumPy magic.
# It returns two arrays (of equal length):
#    1. The list of unique data rows from the input array
#    2. The number of occurrences of each unique row
# Both arrays are sorted in descending order such that the most frequent rows
# are listed first.
def row_histogram(a):
    ca = numpy.ascontiguousarray(a).view([('', a.dtype)] * a.shape[1])
    unique, indices, inverse = numpy.unique(ca, return_index=True, return_inverse=True)
    counts = numpy.bincount(inverse)
    sort_indices = numpy.argsort(counts)[::-1]
    return (a[indices[sort_indices]], counts[sort_indices])

# Compute frequency histogram.
unique_indices, counts = row_histogram(voro_indices)

# Print the ten most frequent histogram entries.
for i in range(10):
    print("%s\t%i\t(%.1f %%)" % (tuple(unique_indices[i]),
                                 counts[i],
                                 100.0*float(counts[i])/len(voro_indices)))
