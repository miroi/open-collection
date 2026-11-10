===========================
Hg@Au(111) with Nequip MLIP
===========================

claude ai:
---------
 https://claude.ai/share/81d8a6ee-8585-45f2-91af-37bf923e7ef4

installation into own conda environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MUST BE OWN PYTHON ENVIRONMENT TO AVOID CONFLICTS !!!

conda create -n nequip_env python=3.11 -y
conda activate nequip_env

# CPU-only PyTorch (skip the --index-url line if you want the default build)
pip install torch --index-url https://download.pytorch.org/whl/cpu

pip install nequip ase

.
.
.
Installing collected packages: antlr4-python3-runtime, urllib3, tzdata, tqdm, pyyaml, pyparsing, propcache, pillow, opt-einsum, numpy, multidict, lmdb, lightning-utilities, kiwisolver, idna, frozenlist, fonttools, cycler, charset_normalizer, certifi, attrs, aiohappyeyeballs, yarl, scipy, requests, python-dateutil, omegaconf, contourpy, aiosignal, torchmetrics, opt_einsum_fx, matplotlib, hydra-core, aiohttp, e3nn, ase, pytorch-lightning, matscipy, lightning, nequip
Successfully installed aiohappyeyeballs-2.7.1 aiohttp-3.14.5 aiosignal-1.4.0 antlr4-python3-runtime-4.9.3 ase-3.29.0 attrs-26.1.0 certifi-2026.10.23 charset_normalizer-3.5.2 contourpy-1.3.3 cycler-0.12.1 e3nn-0.6.0 fonttools-4.68.0 frozenlist-1.8.0 hydra-core-1.3.8 idna-3.20 kiwisolver-1.5.1 lightning-2.6.6 lightning-utilities-0.15.3 lmdb-3.0.0 matplotlib-3.11.2 matscipy-1.3.1 multidict-7.2.1 nequip-0.19.1 numpy-2.4.6 omegaconf-2.3.1 opt-einsum-3.4.0 opt_einsum_fx-0.1.4 pillow-13.0.0 propcache-0.5.4 pyparsing-3.3.3 python-dateutil-4.0.0 pytorch-lightning-2.6.6 pyyaml-6.0.3 requests-2.34.2 scipy-1.17.1 torchmetrics-1.9.0 tqdm-4.70.1 tzdata-2026.6 urllib3-2.8.0 yarl-1.25.1

(nequip_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/Hg_on_gold/ML-IP_nequip/.pip show ase nequip
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /home/miroi/miniconda3/envs/nequip_env/lib/python3.11/site-packages
Requires: matplotlib, numpy, scipy, typing_extensions
Required-by: matscipy, nequip
---
Name: nequip
Version: 0.19.1
Summary: NequIP is an open-source code for building E(3)-equivariant interatomic potentials.
Home-page: https://github.com/mir-group/nequip
Author:
Author-email: The NequIP Developers <allegro-nequip@g.harvard.edu>
License: MIT License
.
.

Location: /home/miroi/miniconda3/envs/nequip_env/lib/python3.11/site-packages
Requires: ase, e3nn, hydra-core, lightning, lmdb, matscipy, numpy, pyyaml, requests, torch, torchmetrics, tqdm


Download and compile a foundation model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nequip-compile \
  nequip.net:mir-group/NequIP-OAM-L:0.1 \
  model.nequip.pt2 \
  --device cpu \
  --mode aotinductor \
  --target ase

.
.
[2026-11-10 10:36:08,169][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to model.nequip.pt2


running
-------
python pd_on_gold_nequip.py >  pd_on_gold_nequip.py_logfile


Literature
----------
https://proceedings.spp-online.org/article/view/SPP-2017-PB-21



