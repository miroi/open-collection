=================
ASE driven ALIGNN
=================

https://github.com/usnistgov/alignn

see issue https://github.com/usnistgov/alignn/issues/193

installation
~~~~~~~~~~~~~

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.source ~/work/software/myenv/bin/activate
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip install -q dgl -f https://data.dgl.ai/wheels/torch-2.1/repo.html


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip show dgl
Name: dgl
Version: 2.4.0
Summary: Deep Graph Library
Home-page: https://github.com/dmlc/dgl
Author:
Author-email:
License: APACHE
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: networkx, numpy, packaging, pandas, psutil, pydantic, pyyaml, requests, scipy, torch, tqdm
Required-by:

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip install alignn
.
.
Successfully installed alignn-2025.4.1 dgl-0.1.3 flake8-7.3.0 lmdb-1.7.5 mccabe-0.7.0 numpy-1.26.4 nvidia-cudnn-cu12-8.9.2.26 nvidia-nccl-cu12-2.19.3 pycodestyle-2.14.0 pydocstyle-6.3.0 pyflakes-3.4.0 pyparsing-2.4.7 snowballstemmer-3.0.1 torch-2.2.1

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip show alignn
Name: alignn
Version: 2025.4.1
Summary: alignn
Home-page: https://github.com/usnistgov/alignn
Author: Kamal Choudhary, Brian DeCost
Author-email: kamal.choudhary@nist.gov
License:
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: ase, dgl, flake8, jarvis-tools, lmdb, matplotlib, mpmath, numpy, pandas, pycodestyle, pydantic, pydantic-settings, pydocstyle, pyparsing, scikit-learn, scipy, spglib, torch, tqdm
Required-by:

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip install Mapping
.
.
Successfully installed Mapping-0.1.6 clarabel-0.11.1 cvxpy-1.7.3 osqp-1.0.5 scs-3.2.9

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip show Mapping
Name: mapping
Version: 0.1.6
Summary: Mappings for generic and tradeable futures instruments
Home-page: https://github.com/MatthewGilbert/mapping
Author: Matthew Gilbert
Author-email: matthew.gilbert12@gmail.com
License: MIT
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: cvxpy, numpy, pandas
Required-by:



download
~~~~~~~~

https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Structure_Relaxation_Phonons_Interface.ipynb

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip install -q "phonopy==2.10.0"
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip show phonopy
Name: phonopy
Version: 2.10.0
Summary: This is the phonopy module.
Home-page: http://phonopy.github.io/phonopy/
Author: Atsushi Togo
Author-email: atz.togo@gmail.com
License:
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: h5py, matplotlib, numpy, PyYAML, spglib
Required-by:


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip install -q git+https://github.com/usnistgov/intermat.git@develop

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.pip show intermat
Name: intermat
Version: 2024.5.24
Summary: intermat
Home-page: https://github.com/usnistgov/intermat
Author: Kamal Choudhary
Author-email: kamal.choudhary@nist.gov
License:
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: jarvis-tools, numpy, pydantic_settings, scipy
Required-by:



run
~~~
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/alignn-ase/wsl2/.python alignn_structure_relaxation_phonons_interface.py
.
.
ImportError: cannot import name 'Mapping' from 'collections' (/usr/lib/python3.12/collections/__init__.py)


