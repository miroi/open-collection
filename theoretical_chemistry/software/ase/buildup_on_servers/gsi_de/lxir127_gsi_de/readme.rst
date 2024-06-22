ASE
===

see https://asap3.readthedocs.io/en/latest/installation/Installation.html#optimized-installation

modules
-------

spack unload --all

milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lxir127_gsi_de/.spack load python@3.10.8 target=x86_64
milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lxir127_gsi_de/.spack load py-pip target=x86_64

milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lxir127_gsi_de/.python3 -m pip install --upgrade --user ase

python3 -m pip install --upgrade --user pip

GPAW with ASE
-------------
python3 -m pip install gpaw

Successfully installed gpaw-24.6.0 numpy-1.26.4
