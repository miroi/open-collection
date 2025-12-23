=======================================
MatGL installation on WSL2 Win11 Victus
=======================================


miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/.source ~/work/software/myenv/bin/activate

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/.pip install matgl
.
.
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torchvision 0.24.1 requires torch==2.9.1, but you have torch 2.8.0 which is incompatible.
Successfully installed aiohappyeyeballs-2.6.1 aiohttp-3.13.2 aiosignal-1.4.0 boto3-1.42.14 botocore-1.42.14 frozenlist-1.8.0 jmespath-1.0.1 lightning-2.6.0 matgl-2.0.6 multidict-6.7.0 nvidia-nccl-cu12-2.27.3 propcache-0.4.1 pytorch-lightning-2.6.0 s3transfer-0.16.0 torch-2.8.0 torch-geometric-2.7.0 torchdata-0.11.0 triton-3.4.0 xxhash-3.6.0 yarl-1.22.0

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/tests/.pip show matgl
Name: matgl
Version: 2.0.6
Summary: MatGL is a framework for graph deep learning for materials science.
Home-page:
Author:
Author-email: Tsz Wai Ko <t1ko@ucsd.edu>, Marcel Nassar <marcel.nassar@intel.com>, Ji Qi <j1qi@ucsd.edu>, Santiago Miret <santiago.miret@intel.com>, Eliott Liu <elliottliu17@gmail.com>, Bowen Deng <bowendeng@berkeley.edu>, Luis Barroso-Luque <lbluque@berkeley.edu>, Shyue Ping Ong <ongsp@ucsd.edu>
License: BSD-3-Clause
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: ase, boto3, lightning, numpy, pydantic, pymatgen, torch, torch-geometric, torchdata
Required-by:


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/.which mgl
/home/miroi/work/software/myenv/bin/mgl

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/.mgl --help

usage: mgl [-h] {relax,predict,md,clear} ...


