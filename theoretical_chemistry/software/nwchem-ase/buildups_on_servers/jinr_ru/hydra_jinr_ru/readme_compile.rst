=========================
NWChem buildup on Govorun
=========================

milias@hydra.jinr.ru:~/work/software/nwchem/.wget https://github.com/nwchemgit/nwchem/archive/refs/tags/v7.2.3-release.zip


fix
~~~
https://www.nwchem-sw.org/index-php/Special_AWCforum/st/id1025/Compilation_error_with_include/m---.html
milias@hydra.jinr.ru:~/work/software/nwchem/nwchem-7.2.3-release/src/.rm input/dependencies

compile
~~~~~~~
sbatch compile_release7_2_3-release_slurm.01
