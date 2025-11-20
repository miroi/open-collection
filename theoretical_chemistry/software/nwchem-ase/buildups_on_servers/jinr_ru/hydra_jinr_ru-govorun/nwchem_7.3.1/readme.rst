============
NWChem 7.3.1
============

https://github.com/nwchemgit/nwchem/releases/tag/v7.3.1-release

download
~~~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/packaged/.wget https://github.com/nwchemgit/nwchem/releases/download/v7.3.1-release/nwchem-7.3.1-release.revision-23c3b41b-nonsrconly.2025-11-06.tar.bz2

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/packaged/nwchem-7.3.1/src/nwpw/nwpwlib/nwpwxc/../build_dftd3a.sh
downloading dftd3.tgz
chchc curl -f -L https://www.chemie.uni-bonn.de/grimme/de/software/dft-d3//dftd3.tgz -o dftd3.tgz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  542k  100  542k    0     0   771k      0 --:--:-- --:--:-- --:--:--  772k
patching file nwpwxc_vdw3a.F


compile
~~~~~~~
sbatch hydra_slurm_compile_nwchem.01

problem with python ! see https://groups.google.com/g/nwchem-forum/c/8RPwzel6dZk/m/eC1nKTwfBQAJ


