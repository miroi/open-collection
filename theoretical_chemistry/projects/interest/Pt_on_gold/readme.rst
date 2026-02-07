=======================
Au slab with Pt addatom
=======================

Experimental works:

Gotsis, H. J., I. Rivalta, Emilia Sicilia, and Nino Russo. "Pd, Rh, Ir and Pt adsorption on gold: A theoretical study of different surfaces." Chemical physics letters 442, no. 1-3 (2007): 105-109., doi: https://doi.org/10.1016/j.cplett.2007.05.064 (access https://sci-hub.ru/10.1021/jp5033228 )

Freire, Rafael LH, Adam Kiejna, and Juarez LF Da Silva. "Adsorption of Rh, Pd, Ir, and Pt on the Au (111) and Cu (111) surfaces: a density functional theory investigation." The Journal of Physical Chemistry C 118.33 (2014): 19051-19061., doi: https://doi.org/10.1021/jp5033228 (access https://www.researchgate.net/profile/Juarez-Da-Silva-2/publication/272128588_Adsorption_of_Rh_Pd_Ir_and_Pt_on_the_Au111_and_Cu111_Surfaces_A_Density_Functional_Theory_Investigation/links/6252bf34b0cee02d696130a1/Adsorption-of-Rh-Pd-Ir-and-Pt-on-the-Au111-and-Cu111-Surfaces-A-Density-Functional-Theory-Investigation.pdf)

correction : https://pubs.acs.org/doi/pdf/10.1021/acs.jpcc.5b08430?ref=article_openPDF

take Au(1 1 1) surface (Table 1)


WSL2 on own PC
---------------
python3 Pt_on_Au-slab.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 0.47677295552592724
Pt single atom pot.energy = 5.85
energy of atom plus surface system : 0.6714933807144492
adsorption energy of Pt on Au fcc111 = -5.655279574811478

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.python  Pt_on_Au-slab.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 0.47677295552592724
Pt single atom pot.energy = 5.85
energy of atom plus surface system : 0.6714933807144492
adsorption energy of Pt on Au fcc111 = -5.655279574811478 (exp. cca -4.8 eV)


display trajectory
~~~~~~~~~~~~~~~~~~
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.ase gui Pt_on_Au-slab.traj

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.ase gui Pt_on_Au-slab.traj


