"""An example to use kimpy to compute the energy vs. distance of a copper dimer."""

import numpy as np
import kimpy


# Callback routine for the KIM API to get atom neighbor lists
def get_neigh(data_in, cutoffs_in, neighbor_list_index_in, particle_number_in):
    neighbors = data_in["neighbors"][particle_number_in]
    return (neighbors, 0)


# Function to construct neighbor lists for the atoms.
# (This is a highly-inefficient N^2 algorithm that should only be used for
# small numbers of atoms.)
# For larger systems, you might want to use kimpy.neighlist.
def create_neigh(coords_in, cutoff, neigh_in):
    n = coords_in.shape[0]
    neighbors = []
    for i in range(n):
        neigh_i = []
        for j in range(n):
            if j == i:
                continue
            dist = np.linalg.norm(coords_in[i] - coords_in[j])
            if dist < cutoff:
                neigh_i.append(j)
        neigh_i = np.array(neigh_i, dtype=np.intc)
        neighbors.append(neigh_i)
    neigh_in["cutoff"] = cutoff
    neigh_in["num_particles"] = n
    neigh_in["neighbors"] = neighbors


# Initialize KIM potential specifying the units requested from the potential.
modelname = "EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005"
units_accepted, kim_model = kimpy.model.create(
    kimpy.numbering.zeroBased,
    kimpy.length_unit.A,
    kimpy.energy_unit.eV,
    kimpy.charge_unit.e,
    kimpy.temperature_unit.K,
    kimpy.time_unit.ps,
    modelname,
)


# Define simulation arguments
N = 2
coords = np.zeros((N, 3), dtype=np.double)
forces = np.zeros((N, 3), dtype=np.double)
energy = np.array([0.0], dtype=np.double)
num_particles = np.array([N], dtype=np.intc)
species_code = np.zeros(num_particles, dtype=np.intc)
particle_contributing = np.zeros(num_particles, dtype=np.intc)

# Set KIM API pointers to simulation arguments
compute_arguments = kim_model.compute_arguments_create()
compute_arguments.set_argument_pointer(
    kimpy.compute_argument_name.numberOfParticles, num_particles
)
compute_arguments.set_argument_pointer(
    kimpy.compute_argument_name.particleSpeciesCodes, species_code
)
compute_arguments.set_argument_pointer(
    kimpy.compute_argument_name.particleContributing, particle_contributing
)
compute_arguments.set_argument_pointer(kimpy.compute_argument_name.coordinates, coords)
compute_arguments.set_argument_pointer(
    kimpy.compute_argument_name.partialEnergy, energy
)
compute_arguments.set_argument_pointer(
    kimpy.compute_argument_name.partialForces, forces
)

# Setup neighbor lists through KIM API callback mechanism
neigh = dict()
compute_arguments.set_callback(
    kimpy.compute_callback_name.GetNeighborList, get_neigh, neigh
)

# Setup for calculation
influence_dist = kim_model.get_influence_distance()
supported, code = kim_model.get_species_support_and_code(kimpy.species_name.Al)
species_code[:] = code
particle_contributing[:] = 1

# Loop over dimer energy
print("  Distance", " " * 9, "Energy")
for z in np.arange(1.0, np.ceil(influence_dist) + 0.5, 0.5):
    coords[1, 2] = z
    create_neigh(coords, influence_dist, neigh)
    kim_model.compute(compute_arguments)
    print("{:18.10e} {:18.10e}".format(z, energy[0]))
