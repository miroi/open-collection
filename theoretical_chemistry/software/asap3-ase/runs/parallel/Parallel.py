##
##
##

#SBATCH --partition=xeon8
#SBATCH -N 2
#SBATCH -n 1
#SBATCH --time=0:30:00
#SBATCH --output=ExampleParallel-%J.out

# The comments above makes it possible to submit this script as a PBS job
# to the Niflheim cluster using the asap-sbatch command.


from asap3 import EMT, print_version
# It is important to import file reading/writing and Molecular Dynamics
# from asap3 and not ase in order for parallel simulations to work.
from asap3.io import Trajectory
from asap3.md.langevin import Langevin
from asap3.analysis import PTMobserver
from ase.parallel import paropen, world
from ase import units
from asap3.visualize.primiplotter import ParallelPrimiPlotter, PngFile
import time

infile = "initial.traj"
infofile = "relax-01.txt"
outfile = "relax-01.traj"
plotprefix = "relax-01-"

n_output = 5000    # Plot and save every 5000 time steps
n_summary = 100    # Print a summary line every 100 time steps
n_total = 10 * n_output  # Total simulation length
timestep = 5.0   # fs
lgvfrict = 0.001
temperature = 300 # Kelvin

# Specify the decomposition onto CPU cores 
#cpulayout = (2, 2, 2)    # 8 cores in 2*2*2 grid
cpulayout = "auto"       # Just figure it out...

# Print Asap version
if world.rank == 0:
    print_version(1)

# Open info file with line buffering. Only the master core writes to it.
info = paropen(infofile, "w", 1)
info.write("Simulation started: {0}\n".format(time.ctime()))

# Read the last frame of the input file.  The atoms are distributed among
# processors.
atoms = Trajectory(infile).get_atoms(-1, cpulayout)
nAtoms = atoms.get_number_of_atoms()
info.write("Distribution on CPU cores: {0}\n".format(str(atoms.nCells)))
atoms.set_calculator(EMT())

# Rapidly move the temperature to the desired range by running a
# langevin simulation with increased friction at twice the temperature
# until the desired temperature is crossed.

dyn = Langevin(atoms, timestep * units.fs,
               temperature * 2 * units.kB, 20*lgvfrict)

i = 0
while atoms.get_temperature() < temperature:
    i = i + 1
    dyn.run(10)
    info.write("Energy per atom (step %d): Epot = %.3f eV   Ekin = %.3f eV\n" %
               (i, atoms.get_potential_energy()/nAtoms, atoms.get_kinetic_energy()/nAtoms))
info.write("Temperature has reached %d K: %s\n" % (atoms.get_temperature(), time.ctime()))

# Run the real dynamics
dyn = Langevin(atoms, timestep * units.fs,
               temperature * units.kB, lgvfrict)

# PTM analysis
ptm = PTMobserver(atoms, rmsd_max=0.2, cutoff=5.0)
dyn.attach(ptm.analyze, interval=n_output)

# Output trajectory
writer = Trajectory(outfile, "w", atoms)
ptm.attach(writer)
writer.write()   # Write the initial configuration

# On-the-fly-plotting
def invisible_atoms(a):
    """Return True for atoms that should be invisible."""
    r = atoms.get_positions()
    c = atoms.get_tags()
    cell = atoms.get_cell()
    return (c == 2) | (r[:,1] < 5.0) | (r[:,1] > cell[1,1] - 5)

mycolors = {0: (0.3, 0.3, 1.0),  # Unknown is blue
            1: (0.2, 1.0, 0.2),  # SC is green
            2: (1.0, 1.0, 1.0),  # FCC is white
            3: (1.0, 0.0, 0.0),  # HCP is red
            4: (1.0, 1.0, 0.0),  # ICO is yellow
            5: (0.0, 0.0, 0.0)   # BCC is black
            }

plotter = ParallelPrimiPlotter(atoms)
plotter.set_invisibility_function(invisible_atoms)
plotter.set_colors(mycolors) # Map tags to colors
plotter.set_output(PngFile(plotprefix))
plotter.set_rotation([-88,0,0])
ptm.attach(plotter.plot)
plotter.plot()   # Plot the initial configuration.

# Run the simulation
def summary(atoms=atoms):
    info.write("Energy per atom (step %d): Epot = %.3f eV   Ekin = %.3f eV\n" %
               (i, atoms.get_potential_energy()/nAtoms,
                atoms.get_kinetic_energy()/nAtoms))
    info.write("    Stress: %g %g %g\n            %g %g %g\n" %
               tuple(atoms.get_stress()))

dyn.attach(summary, interval=n_summary)
dyn.run(n_total)

