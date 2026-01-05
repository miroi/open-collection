=======================
MatGL on lxui11.jinr.ru
=======================

milias@lxui11.jinr.ru:~/software/.python -V
Python 3.9.25

milias@lxui11.jinr.ru:~/software/. python -m venv venv

milias@lxui11.jinr.ru:~/git_projects/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/.source ~/software/venv/bin/activate

(venv) milias@lxui11.jinr.ru:~/git_projects/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/lxui11_jinr_ru/.pip install matgl
.
.
.
disk space exceeded !!! use source /cvmfs/bmn.jinr.ru/config/x86_64-alma9/cluster_config.sh
https://bmn.jinr.int/jinr-cicc-complex/


better disk space 
~~~~~~~~~~~~~~~~~
milias@lxui11.jinr.ru:/scr/u/.mkdir milias
milias@lxui11.jinr.ru:/scr/u/.cd milias/
milias@lxui11.jinr.ru:/scr/u/milias/.ls
milias@lxui11.jinr.ru:/scr/u/milias/.python -m venv venv

milias@lxui11.jinr.ru:/scr/u/milias/.
milias@lxui11.jinr.ru:/scr/u/milias/.source venv/bin/activate
(venv) milias@lxui11.jinr.ru:/scr/u/milias/.pip install matgl
.
.
Successfully installed MarkupSafe-3.0.3 PyYAML-6.0.3 aiohappyeyeballs-2.6.1 aiohttp-3.13.3 aiosignal-1.4.0 annotated-types-0.7.0 ase-3.26.0 async-timeout-5.0.1 attrs-25.4.0 boto3-1.42.22 botocore-1.42.22 certifi-2026.1.4 charset-normalizer-3.4.4 contourpy-1.3.0 cycler-0.12.1 dgl-2.1.0 filelock-3.19.1 fonttools-4.60.2 frozenlist-1.8.0 fsspec-2025.10.0 idna-3.11 importlib-metadata-8.7.1 importlib-resources-6.5.2 jinja2-3.1.6 jmespath-1.0.1 joblib-1.5.3 kiwisolver-1.4.7 latexcodec-3.0.1 lightning-2.5.0.post0 lightning-utilities-0.15.2 matgl-1.2.1 matplotlib-3.9.4 monty-2025.3.3 mpmath-1.3.0 multidict-6.7.0 narwhals-2.14.0 networkx-3.2.1 numpy-1.26.4 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.19.3 nvidia-nvjitlink-cu12-12.9.86 nvidia-nvtx-cu12-12.1.105 packaging-24.2 palettable-3.3.3 pandas-2.3.3 pillow-11.3.0 plotly-6.5.0 propcache-0.4.1 psutil-7.2.1 pybtex-0.25.1 pydantic-2.12.5 pydantic-core-2.41.5 pymatgen-2024.8.9 pyparsing-3.3.1 python-dateutil-2.9.0.post0 pytorch-lightning-2.6.0 pytz-2025.2 requests-2.32.5 ruamel.yaml-0.19.1 s3transfer-0.16.0 scipy-1.13.1 six-1.17.0 spglib-2.7.0 sympy-1.14.0 tabulate-0.9.0 torch-2.2.0 torchdata-0.7.1 torchmetrics-1.8.2 tqdm-4.67.1 triton-2.2.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzdata-2025.3 uncertainties-3.2.3 urllib3-1.26.20 yarl-1.22.0 zipp-3.23.0
(venv) milias@lxui11.jinr.ru:/scr/u/milias/.

milias@lxui11.jinr.ru:/scr/u/milias/open-collection/theoretical_chemistry/software/.pip show matgl dgl
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
Required-by: matgla

pip install --upgrade pip

pip show ase
Name: ase
Version: 3.26.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /scr/u/milias/venv/lib/python3.9/site-packages
Requires: matplotlib, numpy, scipy
Required-by: matgl


