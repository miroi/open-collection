from ase.build import molecule
from ase.collections import g2

print(f" Names of available ",len(g2.names), " molecules: ", g2.names)

print("1st molecule  :",g2.names[0])
print("last molecule :",g2.names[len(g2.names)-1])
