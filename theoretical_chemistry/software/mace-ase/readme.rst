=============
MACE with ASE
=============


installation
------------
https://github.com/ACEsuit/mace?tab=readme-ov-file#installation-from-pypi

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.source ~/work/software/myenv/bin/activate
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install --upgrade pip
.
.
      Successfully uninstalled pip-24.0
Successfully installed pip-25.3

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install mace-torch
Collecting mace-torch
.
.
Successfully built python-hostlist
Installing collected packages: python-hostlist, wcwidth, smmap, opt_einsum, lightning-utilities, configargparse, prettytable, gitdb, GitPython, torchmetrics, torch-ema, opt-einsum-fx, matscipy, e3nn, mace-torch
Successfully installed GitPython-3.1.45 configargparse-1.7.1 e3nn-0.4.4 gitdb-4.0.12 lightning-utilities-0.15.2 mace-torch-0.3.14 matscipy-1.1.1 opt-einsum-fx-0.1.4 opt_einsum-3.4.0 prettytable-3.16.0 python-hostlist-2.3.0 smmap-5.0.2 torch-ema-0.3 torchmetrics-1.8.2 wcwidth-0.2.14

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip show mace-torch
Name: mace-torch
Version: 0.3.14
Summary:
Home-page: https://github.com/ACEsuit/mace
Author:
Author-email:
License:
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install mace-torch nglview ipywidgets rdkit x3dase
.
.
.
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install mace-torch nglview ipywidgets rdkit x3daseSuccessfully built nglview
Installing collected packages: webencodings, pure-eval, ptyprocess, fastjsonschema, widgetsnbextension, websocket-client, webcolors, uri-template, traitlets, tornado, tinycss2, soupsieve, sniffio, send2trash, rpds-py, rfc3986-validator, rfc3339-validator, rdkit, pyzmq, python-json-logger, prompt_toolkit, prometheus-client, platformdirs, pexpect, parso, pandocfilters, nest-asyncio, mistune, lark, jupyterlab_widgets, jupyterlab-pygments, jsonpointer, json5, ipython-pygments-lexers, h11, fqdn, executing, defusedxml, decorator, debugpy, comm, bleach, babel, attrs, async-lru, asttokens, terminado, stack_data, rfc3987-syntax, referencing, matplotlib-inline, jupyter-core, jedi, httpcore, beautifulsoup4, arrow, argon2-cffi-bindings, anyio, jupyter-server-terminals, jupyter-client, jsonschema-specifications, isoduration, ipython, httpx, argon2-cffi, x3dase, jsonschema, ipywidgets, ipykernel, nbformat, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shim, jupyterlab-server, jupyter-lsp, jupyterlab, notebook, nglview
Successfully installed anyio-4.11.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 arrow-1.4.0 asttokens-3.0.0 async-lru-2.0.5 attrs-25.4.0 babel-2.17.0 beautifulsoup4-4.14.2 bleach-6.3.0 comm-0.2.3 debugpy-1.8.17 decorator-5.2.1 defusedxml-0.7.1 executing-2.2.1 fastjsonschema-2.21.2 fqdn-1.5.1 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 ipykernel-7.1.0 ipython-9.6.0 ipython-pygments-lexers-1.1.1 ipywidgets-8.1.8 isoduration-20.11.0 jedi-0.19.2 json5-0.12.1 jsonpointer-3.0.0 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 jupyter-client-8.6.3 jupyter-core-5.9.1 jupyter-events-0.12.0 jupyter-lsp-2.3.0 jupyter-server-2.17.0 jupyter-server-terminals-0.5.3 jupyterlab-4.4.10 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.0 jupyterlab_widgets-3.0.16 lark-1.3.1 matplotlib-inline-0.2.1 mistune-3.1.4 nbclient-0.10.2 nbconvert-7.16.6 nbformat-5.10.4 nest-asyncio-1.6.0 nglview-4.0 notebook-7.4.7 notebook-shim-0.2.4 pandocfilters-1.5.1 parso-0.8.5 pexpect-4.9.0 platformdirs-4.5.0 prometheus-client-0.23.1 prompt_toolkit-3.0.52 ptyprocess-0.7.0 pure-eval-0.2.3 python-json-logger-4.0.0 pyzmq-27.1.0 rdkit-2025.9.1 referencing-0.37.0 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rpds-py-0.28.0 send2trash-1.8.3 sniffio-1.3.1 soupsieve-2.8 stack_data-0.6.3 terminado-0.18.1 tinycss2-1.4.0 tornado-6.5.2 traitlets-5.14.3 uri-template-1.3.0 webcolors-25.10.0 webencodings-0.5.1 websocket-client-1.9.0 widgetsnbextension-4.0.15 x3dase-1.1.4


documentation
~~~~~~~~~~~~~

https://mace-docs.readthedocs.io/en/latest




