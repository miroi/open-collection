===================
DeePMD-kit with ASE
===================

https://github.com/deepmodeling/deepmd-kit

https://docs.deepmodeling.com/projects/deepmd/en/stable/

installation
------------
conda create -n deepmd deepmd-kit ase lammps horovod -c conda-forge

done
#
# To activate this environment, use
#
#     $ conda activate deepmd
#
# To deactivate an active environment, use
#
#     $ conda deactivate

list all packages
~~~~~~~~~~~~~~~~~
conda list > conda_list.logfile

test
----
wget https://bohrium-api.dp.tech/ds-dl/DeePMD-kit-Tutorial-a8z5-v1.zip
cp DeePMD-kit_Tutorial/01.train.finished/graph.pb  .

python methane_ase_dp.py > methane_ase_dp.py_logfile

