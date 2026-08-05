==============
DALTON program
==============

web
---
https://daltonproject.readthedocs.io/en/latest/#

https://gitlab.com/dalton/dalton

download
--------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dalton/.git clone git@gitlab.com:dalton/dalton.git dalton_cloned

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dalton/dalton_cloned/.gsu
Submodule 'external/gen1int' (https://gitlab.com/bingao/gen1int.git) registered for path 'external/gen1int'
Submodule 'external/pelib' (https://gitlab.com/pe-software/pelib.git) registered for path 'external/pelib'
Cloning into '/lustre/projects/m/milias/work/software/dalton/dalton_cloned/external/gen1int'...
Cloning into '/lustre/projects/m/milias/work/software/dalton/dalton_cloned/external/pelib'...
Submodule path 'external/gen1int': checked out 'a9893e074d4f51357b0ea95b2af33a5ee601dd61'
Submodule path 'external/pelib': checked out '79f54ecf9c4268d3e98a8bdbdb1bccc0744cdaa6'


buildup with ctests
-------------------
sbatch hydra_slurm_dalton_buildup_ctest.01
