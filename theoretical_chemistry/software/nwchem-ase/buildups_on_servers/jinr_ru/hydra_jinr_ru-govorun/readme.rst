=========================
NWChem buildup on Govorun
=========================

download & clone
~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/nwchem/.wget https://github.com/nwchemgit/nwchem/releases/download/v7.2.3-release/nwchem-7.2.3-release.revision-d690e065-src.2024-08-27.tar.bz2

milias@hydra.jinr.ru:~/work/software/nwchem/.nohup git clone git@github.com:nwemgit/nwchem.git nwchem_master  &
[1] 54702

compile
~~~~~~~
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/nwchem-ase/buildups_on_servers/jinr_ru/hydra_jinr_ru/.nohup compile_nwchem-master_bash.01 &
[1] 55493

#sbatch compile_nwchem-7_2_3-slurm.01


