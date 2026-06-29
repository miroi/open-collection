Simple test ASE-Gromacs
=======================

python script:
https://share.google/aimode/am2hqq2m5HuAHYoSH

pdb: https://share.google/aimode/e5nuCEqSyzNzVCqoR
 from https://www.rcsb.org/structure/1CRN

run
---

https://chat.deepseek.com/a/chat/s/56441f7a-73e5-4a8a-9fa4-9c2e33a622c1


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.python gromacs_ase_example.py > gromacs_ase_example.py_logfile

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.ls
'#gromacs.g96.1#'       gromacs.edr          gromacs.log           gromacs.tpr                            gromacs_ase_example_02.py   posre.itp
 1CRN.pdb               gromacs.g96          gromacs.mdp           gromacs.trr                            inputGenergy.txt            readme.rst
 MM.log                 gromacs.genbox.log   gromacs.pdb2gmx.log   gromacs_ase_example.py                 inputGtraj.txt
 gromacs.editconf.log   gromacs.grompp.log   gromacs.top           gromacs_ase_example.py_logfile_SAVED   mdout.mdp



(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.python gromacs_ase_example_02.py  >  gromacs_ase_example_02.py_logfile


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.ls
1CRN.pdb            gromacs.g96             gromacs_ase_example.py_logfile_SAVED     mdout.mdp  minim.log  minim.trr  nvt.gro  nvt.tpr    readme.rst
box.g96             gromacs.top             gromacs_ase_example_02.py                minim.edr  minim.mdp  nvt.cpt    nvt.log  nvt.trr
energy_profile.xvg  gromacs_ase_example.py  gromacs_ase_example_02.py_logfile_SAVED  minim.gro  minim.tpr  nvt.edr    nvt.mdp  posre.itp


miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.python   gromacs_ase_example_03.py > gromacs_ase_example_03.py_logfile

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs-ase/runs/ase-test/.ls
1CRN.pdb            gromacs.top                              gromacs_ase_example_03.py                minim.edr  minim.trr  nvt.mdp     rmsd.png
box.g96             gromacs_ase_example.py                   gromacs_ase_example_03.py_logfile_SAVED  minim.gro  nvt.cpt    nvt.tpr     rmsd.xvg
energy_profile.png  gromacs_ase_example.py_logfile_SAVED     gyrate.png                               minim.log  nvt.edr    nvt.trr     temperature.xvg
energy_profile.xvg  gromacs_ase_example_02.py                gyrate.xvg                               minim.mdp  nvt.gro    posre.itp   workflow_20260630_000639.log
gromacs.g96         gromacs_ase_example_02.py_logfile_SAVED  mdout.mdp                                minim.tpr  nvt.log    readme.rst


