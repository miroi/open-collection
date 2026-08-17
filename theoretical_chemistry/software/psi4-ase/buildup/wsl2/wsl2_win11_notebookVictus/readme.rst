=============================
ASE-Psi4 installation on WSL2
=============================

conda create -n psi4env

#
# To activate this environment, use
#
#     $ conda activate psi4env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

conda config --add channels conda-forge
conda config --set channel_priority strict

conda install psi4 -y

(psi4env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/psi4-ase/buildup/wsl2/wsl2_win11_notebookVictus/.psi4 --version
1.11

ASE
~~~
(psi4env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/psi4-ase/buildup/wsl2/wsl2_win11_notebookVictus/.conda install ase  -y

(psi4env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/psi4-ase/buildup/wsl2/wsl2_win11_notebookVictus/.ase --version
ase-3.29.0





