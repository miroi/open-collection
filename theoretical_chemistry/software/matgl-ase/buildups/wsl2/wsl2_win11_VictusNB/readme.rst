=======================================
MatGL installation on WSL2 Win11 Victus
=======================================

empty python environment:

(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.pip list
Package Version
------- -------
pip     24.0
(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.pip install matgl

(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.pip show matgl
Name: matgl
Version: 4.0.2
Summary: MatGL is a framework for graph deep learning for materials science.
Home-page:
Author:
Author-email: Tsz Wai Ko <t1ko@ucsd.edu>, Marcel Nassar <marcel.nassar@intel.com>, Ji Qi <j1qi@ucsd.edu>, Santiago Miret <santiago.miret@intel.com>, Eliott Liu <elliottliu17@gmail.com>, Bowen Deng <bowendeng@berkeley.edu>, Luis Barroso-Luque <lbluque@berkeley.edu>, Shyue Ping Ong <shyue@nus.edu.sg>
License: BSD-3-Clause
Location: /home/miroi/work/software/myenv3/lib/python3.12/site-packages
Requires: ase, boto3, huggingface_hub, lightning, numpy, pydantic, pymatgen-core, torch, torch-geometric, torchdata
Required-by:


(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.which mgl
/home/miroi/work/software/myenv3/bin/mgl
(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.mgl --help
usage: mgl [-h] {relax,predict,md,clear} ...

(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/.pip install  pymatgen
.
.
Installing collected packages: pymatgen
Successfully installed pymatgen-2026.5.4



