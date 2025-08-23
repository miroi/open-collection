from asap3 import *
from asap3.md.verlet import VelocityVerlet
from ase.lattice.cubic import FaceCenteredCubic
#from asap3.io.trajectory import *
from ase.io.trajectory import *
from ase.io import write
from numpy import *
import sys, os, time
from asap3.testtools import ReportTest

#DebugOutput("output.%d")
print_version(1)
delete = True
precision = 1e-8

def maketraj(atoms, t, nstep):
    e = [atoms.get_potential_energy()]
    dyn = VelocityVerlet(atoms, 5*units.fs)
    for i in range(nstep):
        dyn.run(10)
        e.append(atoms.get_potential_energy())
        if t is not None:
            t.write()
    return e

def maketraj_no_e(atoms, t, nstep):
    dyn = VelocityVerlet(atoms, 5*units.fs)
    for i in range(nstep):
        dyn.run(10)
        if t is not None:
            t.write()

def checktraj(t, e, recalc=True):
    i = 0
    for atoms in t:
        if recalc:
            atoms.calc = EMT()
        ReportTest("Checking frame %d" % (i,), atoms.get_potential_energy(),
                   e[i], precision)
        i += 1

initial = FaceCenteredCubic(size=(10,10,10), symbol="Cu", pbc=(1,0,0))


atoms = initial.copy()
atoms.calc = EMT()
atoms.get_potential_energy()
atoms.get_forces()
print("Writing trajectory")
traj = Trajectory("traj1.traj", "w", atoms)
traj.write()
energies = maketraj(atoms, traj, 10)
traj.close()

print("Reading trajectory (recalculating energies)")
traj = Trajectory("traj1.traj")
checktraj(traj, energies)

print("Reading trajectory (stored energies)")
traj = Trajectory("traj1.traj")
checktraj(traj, energies, recalc=False)

print("Repeating simulation")
atoms = traj[5]
atoms.calc = EMT()
energies2 = maketraj(atoms, None, 5)
for i in range(5):
    ReportTest("Rerun[%d]" % (i,), energies2[i], energies[i+5], precision)
traj.close()

print("Appending to trajectory")
atoms = Trajectory("traj1.traj")[-1]
atoms.calc = EMT()
traj = Trajectory("traj1.traj", "a", atoms)
energies2 = maketraj(atoms, traj, 5)
traj.close()

print("Reading longer trajectory")
traj = Trajectory("traj1.traj")
checktraj(traj, energies + energies2[1:])

print("Writing trajectory with write")
write("traj2.traj", atoms)

print("Writing a trajectory without precalculated energies.")
atoms = initial.copy()
atoms.calc = EMT()
traj = Trajectory("traj3.traj", "w", atoms)
traj.write()
maketraj_no_e(atoms, traj, 10)
traj.close()
#traj = Trajectory("traj3.traj")
#checktraj(traj, energies, recalc=False)

if delete:
    print("Deleting trajectory")
    os.unlink("traj1.traj")
    os.unlink("traj2.traj")
    os.unlink("traj3.traj")
    
ReportTest.Summary()
