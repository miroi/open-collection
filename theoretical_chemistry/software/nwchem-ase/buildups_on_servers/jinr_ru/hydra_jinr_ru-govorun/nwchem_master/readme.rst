=====================
NWCHEM-master buildup
=====================

downloading
~~~~~~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/cloned/nwchem_master/src/tools/.get-tools-github
downloading ga-5.9.2.tar.gz from https://github.com/GlobalArrays/ga/releases/download/v5.9.2/ga-5.9.2.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 8343k  100 8343k    0     0  5999k      0  0:00:01  0:00:01 --:--:-- 5999k
ga-5.9.2.tar.gz file integrity OK
patched
configure present. no autogen.sh required

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/cloned/nwchem_master/src/nwpw/nwpwlib/nwpwxc/../build_dftd3a.sh
downloading dftd3.tgz
chchc curl -f -L https://www.chemie.uni-bonn.de/grimme/de/software/dft-d3//dftd3.tgz -o dftd3.tgz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  542k  100  542k    0     0   838k      0 --:--:-- --:--:-- --:--:--  837k
patching file nwpwxc_vdw3a.F

configure & compile
~~~~~~~~~~~~~~~~~~~
sbatch hydra_slurm_compile_nwchem.01
