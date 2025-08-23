"""Usage: python SpecialEMT.py [init]

Used to test if the EMT potential still produces the same energies,
forces and stresses as it used to.  It tests all elements with the
standard EMT parameters, including alloys, and also the special
parameters for Ruthenium and for CuMg and CuZr metallic glasses.

Call it the first time with the "init" argument to generate a data file.

Subsequent calls calculate the same quantities, but compare them with the
database.
"""


from asap3 import *
import pickle
import os, sys, time
from asap3.testtools import ReportTest
from ase.lattice.cubic import *
from ase.lattice.hexagonal import *
from ase.lattice.compounds import *

print_version(1)
datafile = "SpecialEMT.pickle"
CuMgdat = "../doc/EMT-MgCu-glass.dat"
CuZrdat = "../doc/EMT-CuZr-glass.dat"

picklehack = {'encoding': 'latin1'}
    
if len(sys.argv) > 1:
    if len(sys.argv) == 2 and sys.argv[1] == "init":
        init = True
    else:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
else:
    init = False

if init:
    data = {}
else:
    try:
        data = pickle.load(open(datafile, "rb"), **picklehack)
    except OSError:
        print("\n\n", __doc__, "\n\n", file=sys.stderr)
        raise

def check(a, key):
    global data
    print("Testing", key)
    expected_n = data[key+"_n"]
    expected_e = data[key+"_e"]
    expected_f = data[key+"_f"]
    e = a.get_potential_energies()
    f = a.get_forces().ravel()
    ReportTest(f"Number of atoms ({key})", len(a), expected_n, 0)
    ReportTest(f"Energies ({key})", max(np.fabs(e-expected_e)), 0.0, 1e-8)
    ReportTest(f"Forces ({key})", max(np.fabs(f-expected_f)), 0.0, 1e-8)

def generate(a, key):
    global data
    e = a.get_potential_energies()
    f = a.get_forces().ravel()
    n = len(a)
    data[key+"_n"] = n
    data[key+"_e"] = e
    data[key+"_f"] = f

elements = ["Al", "Ni", "Cu", "Pd", "Ag", "Pt", "Au"]
print("Checking single elements")
for e in elements:
    atoms = FaceCenteredCubic(size=(4,4,4), symbol=e, pbc=False)
    atoms.calc = EMT()
    if init:
        generate(atoms, e)
    else:
        check(atoms, e)

print("Checking B2 alloys")
for i in range(1, len(elements)):
    e1 = elements[i]
    e2 = elements[i-1]
    atoms = B2(size=(4,4,4), symbol=(e1,e2), latticeconstant=3.5, pbc=False)
    atoms.calc = EMT()
    if init:
        generate(atoms, e1+e2)
    else:
        check(atoms, e1+e2)

print("Checking Ruthenium")
atoms = HexagonalClosedPacked(directions=[[1,0,-1,0],[0,1,-1,0],[0,0,0,1]],
                              size=(4,4,4), symbol="Ru", pbc=False)
atoms.calc = EMT(EMThcpParameters())
if init:
    generate(atoms, "Ru")
else:
    check(atoms, "Ru")

print("Checking metallic glasses")
for e1, e2 in (("Cu", "Mg"), ("Cu", "Zr")):
    atoms = B2(size=(4,4,4), symbol=(e1,e2), latticeconstant=3.5, pbc=False)
    atoms.calc = EMT(EMTMetalGlassParameters())
    if init:
        generate(atoms, e1+e2)
    else:
        check(atoms, e1+e2)


if init:
    f = open(datafile, "wb")
    dump(data, f)
    f.close()
    print("\nData file initialized.")
    
    
