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
milias@hydra.jinr.ru:~/work/software/nwchem/.nohup: ignoring input and appendi output to ‘nohup.out’


fix
~~~
https://www.nwchem-sw.org/index-php/Special_AWCforum/st/id1025/Compilation_error_with_include/m---.html
milias@hydra.jinr.ru:~/work/software/nwchem/nwchem-7.2.3-release/src/.rm input/dependencies

compile
~~~~~~~
sbatch compile_nwchem-7_2_3-slurm.01
