#  https://aitomistic.com/mlatom/get_started.html#python-api
import mlatom as ml

mol = ml.data.molecule.from_xyz_string('''3

O    0.00000    0.00000    0.11779
H    0.00000    0.75545   -0.47116
H    0.00000   -0.75545   -0.47116
''')
aiqm2 = ml.methods(method='AIQM2')
opt = ml.optimize_geometry(model=aiqm2, initial_molecule=mol).optimized_molecule
print(opt.energy)          # optimized energy in hartree

