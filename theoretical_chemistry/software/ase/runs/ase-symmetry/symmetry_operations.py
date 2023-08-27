#
#  https://github.com/ajjackson/ase-tutorial-symmetry/blob/master/ase-symmetry.md#getting-the-symmetry-operations
#

import ase.spacegroup

spg = ase.spacegroup.Spacegroup(152)
print("Is a-quartz centrosymmetric? {}".format("yes" if spg.centrosymmetric else "no"))
print("Is the a-quartz lattice primitive? {}".format("yes" if spg.lattice == 'P' else "no"))
print("What symbol is this spacegroup? {}".format(spg.symbol))

for i, (rot, trans) in enumerate(spg.get_symop()):
    print("Symmetry operation #{}".format(i + 1))
    print("Rotation matrix: ", rot[0,:])
    print("                 ", rot[1,:])
    print("                 ", rot[2,:])
    print("Translation vector: ", trans)
    print()

