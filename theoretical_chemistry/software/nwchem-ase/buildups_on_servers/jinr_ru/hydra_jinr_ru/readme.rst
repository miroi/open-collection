=========================
NWChem buildup on Govorun
=========================

download
~~~~~~~~
milias@hydra.jinr.ru:~/work/software/nwchem/.wget https://github.com/nwchemgit/nwchem/releases/download/v7.2.3-release/nwchem-7.2.3-release.revision-d690e065-src.2024-08-27.tar.bz2

clone
~~~~~
milias@hydra.jinr.ru:~/work/software/nwchem/.nohup git clone git@github.com:nwemgit/nwchem.git nwchem_master  &
[1] 54702

ga
~~
milias@hydra.jinr.ru:~/work/software/nwchem/nwchem_master/src/tools/.get-tools-github
downloading ga-5.8.2.tar.gz from https://github.com/GlobalArrays/ga/releases/download/v5.8.2/ga-5.8.2.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 8967k  100 8967k    0     0  5821k      0  0:00:01  0:00:01 --:--:-- 27.8M
ga-5.8.2.tar.gz file integrity OK
gamalloc.patch applied
strdup.patch applied
mpipr-too-many.patch applied
ga_ma_align.patch applied
scalapacki4.patch applied
ga_diag_seg_i4.patch applied
autoconf.patch applied
patched
configure present. no autogen.sh required


fix
~~~
https://www.nwchem-sw.org/index-php/Special_AWCforum/st/id1025/Compilation_error_with_include/m---.html
milias@hydra.jinr.ru:~/work/software/nwchem/nwchem-7.2.3-release/src/.rm input/dependencies

compile
~~~~~~~
sbatch compile_nwchem-7_2_3-slurm.01
