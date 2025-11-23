#!/usr/bin/env python
import os
import numpy as np
from ase import Atoms
from ase.build import add_adsorbate
from ase.calculators.lj import LennardJones
#from dftd4.ase import DFTD4
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
from ase.calculators.mixing import SumCalculator
#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#direct-inference-static-calculation
#
from chgnet.model.model import CHGNet
from pymatgen.core import Structure
from chgnet.model import StructOptimizer

chgnet = CHGNet.load()


# Create output directories
os.makedirs('vasp_outputs', exist_ok=True)
os.makedirs('ase_outputs', exist_ok=True)
os.makedirs('traj_files', exist_ok=True)

# ==============================================
# 1. Load Slab
# ==============================================
atoms = Atoms(
    symbols=['Se']*54,
    positions=[ # positions in Angstrom 
        [1.650889131500000, 1.683746901700000, 3.783380037500000],
        [3.900276344333259, 1.728548035370332, 7.183071026661340],
        [3.164291999300000, 3.359224114200000, 2.889699858800000],
        [1.026186625175000, 3.424025517244013, 6.363253496787836],
        [1.709693003400000, 0.013789493200000, 2.072591142200000],
        [3.816802862077331, 0.041143806872806, 5.475286718434903],
        [6.000578278100000, 1.683748763000000, 3.783377838800000],
        [8.253046857091022, 1.729320969581304, 7.182913439546119],
        [7.513978508200000, 3.359225657000000, 2.889693289100000],
        [5.366106543348725, 3.423044786289370, 6.365655397116457],
        [6.059376953100000, 0.013790647800000, 2.072589095600000],
        [8.167321598036818, 0.041104625244312, 5.476852422731121],
        [10.350272451400000, 1.683746522300000, 3.783371018600000],
        [12.610515522478977, 1.729412207919081, 7.183251210217395],
        [11.863676610300001, 3.359223567100000, 2.889693260200000],
        [9.718675049118037, 3.423344518417299, 6.365216138795603],
        [10.409077360000000, 0.013788365400000, 2.072583447500000],
        [12.521954576373018, 0.041476009683691, 5.477237072808205],
        [1.650685537500000, 6.728018218200000, 3.783311734000000],
        [3.900161495344923, 6.772828049536868, 7.182875749737472],
        [3.163992693200000, 8.403927688300000, 2.889889019400000],
        [1.026101347238543, 8.468478459755682, 6.363213627713580],
        [1.709697366400000, 5.058520193000000, 2.072167357100000],
        [3.816688683871375, 5.085606368912565, 5.475051586432720],
        [6.000374654200000, 6.728020131900000, 3.783309492900000],
        [8.252949880710576, 6.773600531750263, 7.182727767482691],
        [7.513679200400000, 8.403929196400000, 2.889882503100000],
        [5.366024654741052, 8.467497866870296, 6.365622927950579],
        [6.059381334000000, 5.058521299700000, 2.072165276000000],
        [8.167194300509948, 5.085567481499835, 5.476623207238730],
        [10.350069037700001, 6.728017886500000, 3.783302582000000],
        [12.610398134015655, 6.773688897439876, 7.183058415709605],
        [11.863377332300001, 8.403927125099999, 2.889882395000000],
        [9.718618586022600, 8.467790554948238, 6.365188230683102],
        [10.409081731100001, 5.058518965800000, 2.072159530100000],
        [12.521826423747234, 5.085933665704721, 5.477005428337980],
        [1.650653867500000, 11.772712430800000, 3.783912896800000],
        [3.900165325399797, 11.817326511274514, 7.183115914790769],
        [3.164256279900000, 13.448070690600000, 2.890355002900000],
        [1.026075922763475, 13.513032362289826, 6.363552145787086],
        [1.709443498800000, 10.103296395499999, 2.072601989100000],
        [3.816739525119851, 10.130097808172051, 5.475170543538957],
        [6.000342828900000, 11.772714306999999, 3.783910584100000],
        [8.252941624360446, 11.818110764623851, 7.182949871833987],
        [7.513942704900000, 13.448072202200001, 2.890348492800000],
        [5.365992260477295, 13.512053087609090, 6.365941143895453],
        [6.059127415800000, 10.103297512899999, 2.072599928400000],
        [8.167263635768563, 10.130053182940449, 5.476743603791574],
        [10.350037238900001, 11.772712022700000, 3.783903807600000],
        [12.610382753041891, 11.818200742166791, 7.183297754728079],
        [11.863640902900000, 13.448070092900000, 2.890348365600000],
        [9.718585375245112, 13.512354262023651, 6.365497340619249],
        [10.408827959800000, 10.103295389600000, 2.072594128500000],
        [12.521874806924485, 10.130430339068111, 5.477125921829531]
    ],
    cell=[ # values in Angstrom
        [13.049072483000000, 0.000001159000000, 0.000000000000000],
        [0.000000444000000, 15.133480000000000, 0.000000000000000],
        [0.000000000000000, 0.000000000000000, 17.485799789000001]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 2. Define all unique adsorption sites
# ==============================================
def get_adsorption_sites(slab):
    sites = {}
    
    # 1. Top sites (all Se atoms)
    for i, atom in enumerate(slab):
        sites[f'top_{i}'] = {'position': atom.position[:2], 'height': 2.5}
    
    # 2. Bridge sites (all unique nearest-neighbor pairs)
    for i in range(len(slab)-1):
        for j in range(i+1, min(i+4, len(slab))):  # Check 3 nearest neighbors
            pos0 = slab[i].position
            pos1 = slab[j].position
            dist = ((pos0[0]-pos1[0])**2 + (pos0[1]-pos1[1])**2)**0.5
            if dist < 3.0:  # Only consider close pairs
                sites[f'bridge_{i}-{j}'] = {
                    'position': [(pos0[0]+pos1[0])/2, (pos0[1]+pos1[1])/2],
                    'height': 2.0
                }
    
    # 3. Hollow sites (all unique triplets)
    for i in range(len(slab)-2):
        for j in range(i+1, len(slab)-1):
            for k in range(j+1, len(slab)):
                pos0 = slab[i].position
                pos1 = slab[j].position
                pos2 = slab[k].position
                # Check if they form a triangle
                if all(((pos0[l]-pos1[l])**2 + (pos1[l]-pos2[l])**2)**0.5 < 3.0 for l in range(2)):
                    sites[f'hollow_{i}-{j}-{k}'] = {
                        'position': [(pos0[0]+pos1[0]+pos2[0])/3, (pos0[1]+pos1[1]+pos2[1])/3],
                        'height': 1.8
                    }
    
    # 4. Channel sites (grid points between chains)
    for x in np.linspace(2, 11, 5):  # 5 points along x
        for y in np.linspace(2, 13, 5):  # 5 points along y
            sites[f'channel_{x:.1f}_{y:.1f}'] = {'position': [x, y], 'height': 2.2}
    
    return sites

# ==============================================
# 3. Screening with LennardJones,CHGNet
# ==============================================
def screen_adsorption_sites(slab, sites):
    energies = {}
    hg = Atoms('Hg', positions=[(0, 0, 0)])
    
    for name, site in sites.items():
        slab_with_hg = slab.copy()
        add_adsorbate(slab_with_hg, hg, height=site['height'], position=site['position'])
        
        # Explicitly fix all original Se atoms (indices 0-53)
        se_indices = list(range(len(slab)))  # [0,1,2,...,53]
        constraint = FixAtoms(indices=se_indices)
        slab_with_hg.set_constraint(constraint)
        
        # Debug print
        print(f"\nSite {name}:")
        print(f"Fixed {len(se_indices)} Se atoms (last Se index: {se_indices[-1]})")
        print(f"Hg atom index: {len(slab_with_hg)-1}, should be free to move")
        
        # Calculator setup
        lj_params = {
            'epsilon': 0.025,  # eV
            'sigma': 2.75,     # Å
            'rc': 10.0         # Cutoff radius
        }
       # slab_with_hg.calc = SumCalculator([
       #     LennardJones(**lj_params),
       #     DFTD4(method="PBE") ])


        #slab_with_hg.calc = SumCalculator([LennardJones(**lj_params) ])
        #relaxer = StructOptimizer()
        #slab_with_hg.calc = SumCalculator(relaxer)


        relaxer = StructOptimizer()
        #result = relaxer.relax(slab_with_hg, fmax=1.00)
        result = relaxer.relax(slab_with_hg, fmax=1.00)

        # Relax only Hg
        relax = BFGS(slab_with_hg, trajectory=f'traj_files/hg_{name}.traj')  # Moved to traj_files
        relax.run(fmax=0.05)
        
        energies[name] = slab_with_hg.get_potential_energy()
        
        # Export to VASP with .vasp extension
        write(f'vasp_outputs/{name}.vasp', slab_with_hg, format='vasp')
        
        # Export to ASE format with improved formatting
        with open(f'ase_outputs/{name}.ase', 'w') as f:
            f.write("from ase import Atoms\n\n")
            f.write("atoms = Atoms(\n")
            f.write(f"    symbols=['Se']*{len(slab)} + ['Hg'],\n")  # Cleaner symbols format
            
            # Positions with each atom on new line
            f.write("    positions=[\n")
            for pos in slab_with_hg.get_positions():
                f.write(f"        [{pos[0]:.10f}, {pos[1]:.10f}, {pos[2]:.10f}],\n")
            f.write("    ],\n")
            
            # Cell vectors
            f.write("    cell=[\n")
            for vec in slab_with_hg.get_cell():
                f.write(f"        [{vec[0]:.10f}, {vec[1]:.10f}, {vec[2]:.10f}],\n")
            f.write("    ],\n")
            
            f.write(f"    pbc={slab_with_hg.pbc.tolist()}\n")
            f.write(")\n")
    
    return energies

# ==============================================
# 4. Run and Save Results
# ==============================================
if __name__ == "__main__":
    sites = get_adsorption_sites(atoms)
    print(f"\nTesting {len(sites)} adsorption sites...\n")
    energies = screen_adsorption_sites(atoms, sites)
    
    # Find best site(s)
    min_energy = min(energies.values())
    best_sites = [site for site, energy in energies.items() if energy == min_energy]
    
    # Write summary file
    with open('adsorption_summary.txt', 'w') as f:
        # Header
        f.write(f"Number of sites tested: {len(sites)}\n")
        f.write(f"Most stable configuration(s): {', '.join(best_sites)}\n")
        f.write(f"Minimum energy: {min_energy:.6f} eV\n\n")
        
        # Energy table
        f.write("Site\t\t\tEnergy (eV)\n")
        f.write("="*40 + "\n")
        for name, energy in sorted(energies.items(), key=lambda x: x[1]):
            f.write(f"{name:30s}\t{energy:.6f}\n")
            if energy == min_energy:
                f.write(" "*-30 + "\t<--- Most stable\n")
    
    # Console output
    print(f"\nMost stable configuration(s): {', '.join(best_sites)}")
    print(f"Minimum energy: {min_energy:.6f} eV\n")
    print("Complete energy table:")
    print("Site\t\t\tEnergy (eV)")
    print("="*50)
    for name, energy in sorted(energies.items(), key=lambda x: x[1]):
        print(f"{name:30s}\t{energy:.6f}", end="")
        if energy == min_energy:
            print(" <--- Most stable", end="")
        print()
