from ase.build import bulk
#from ase.build import cell
si = bulk('Si', 'diamond', a=5.459)
lat = si.cell.get_bravais_lattice()
print(list(lat.get_special_points()))
path = si.cell.bandpath('GXW', npoints=100)
print(path.kpts.shape)
