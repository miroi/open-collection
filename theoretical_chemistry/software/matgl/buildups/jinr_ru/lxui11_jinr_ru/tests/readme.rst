=============================
MatGL test on @lxui11.jinr.ru
=============================


(venv) milias@lxui11.jinr.ru:/scr/u/milias/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/tests/.pip install matgl[dgl]

(venv) milias@lxui11.jinr.ru:/scr/u/milias/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/tests/.python formation_energy_CsCl_dglbackend.py
Traceback (most recent call last):
  File "/scr/u/milias/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/tests/formation_energy_CsCl_dglbackend.py", line 6, in <module>
    matgl.set_backend("DGL")
AttributeError: module 'matgl' has no attribute 'set_backend'

(venv) milias@lxui11.jinr.ru:/scr/u/milias/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/tests/.pip show matgl dgl
Name: matgl
Version: 1.2.1
Summary: MatGL is a framework for graph deep learning for materials science.
Home-page:
Author:
Author-email: Tsz Wai Ko <t1ko@ucsd.edu>, Marcel Nassar <marcel.nassar@intel.com>, Ji Qi <j1qi@ucsd.edu>, Santiago Miret <santiago.miret@intel.com>, Eliott Liu <elliottliu17@gmail.com>, Bowen Deng <bowendeng@berkeley.edu>, Luis Barroso-Luque <lbluque@berkeley.edu>, Shyue Ping Ong <ongsp@ucsd.edu>
License: BSD-3-Clause
Location: /scr/u/milias/venv/lib/python3.9/site-packages
Requires: ase, boto3, dgl, lightning, numpy, pydantic, pymatgen, torch, torchdata
Required-by:
---
Name: dgl
Version: 2.1.0
Summary: Deep Graph Library
Home-page: https://github.com/dmlc/dgl
Author:
Author-email:
License: APACHE
Location: /scr/u/milias/venv/lib/python3.9/site-packages
Requires: networkx, numpy, psutil, requests, scipy, torchdata, tqdm
Required-by: matgl

