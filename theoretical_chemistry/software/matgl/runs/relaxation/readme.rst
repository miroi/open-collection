

https://matgl.ai/tutorials%2FRelaxations%20and%20Simulations%20using%20the%20M3GNet%20Universal%20Potential.html


This notebook demonstrates the use of the pre-trained universal potentials to perform structural relaxations, molecular dynamics simulations and single-point calculations.


(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/runs/relaxation/.python relax.py
Traceback (most recent call last):
  File "/home/miroi/software/venv/lib/python3.12/site-packages/matgl/utils/io.py", line 244, in load_model
    return cls_.load(fpaths, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/matgl/utils/io.py", line 157, in load
    mod = __import__(modname, globals(), locals(), [classname], 0)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/matgl/models/__init__.py", line 10, in <module>
    from ._chgnet import CHGNet
  File "/home/miroi/software/venv/lib/python3.12/site-packages/matgl/models/_chgnet.py", line 19, in <module>
    from dgl import readout_edges, readout_nodes
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/__init__.py", line 16, in <module>
    from . import (
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/dataloading/__init__.py", line 13, in <module>
    from .dataloader import *
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/dataloading/dataloader.py", line 27, in <module>
    from ..distributed import DistGraph
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/distributed/__init__.py", line 5, in <module>
    from .dist_graph import DistGraph, DistGraphServer, edge_split, node_split
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/distributed/dist_graph.py", line 11, in <module>
    from .. import backend as F, graphbolt as gb, heterograph_index
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/graphbolt/__init__.py", line 8, in <module>
    from .base import *
  File "/home/miroi/software/venv/lib/python3.12/site-packages/dgl/graphbolt/base.py", line 8, in <module>
    from torchdata.datapipes.iter import IterDataPipe
ModuleNotFoundError: No module named 'torchdata.datapipes'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/matgl/runs/relaxation/relax.py", line 17, in <module>
    pot = matgl.load_model("M3GNet-MP-2021.2.8-PES")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/matgl/utils/io.py", line 246, in load_model
    raise ValueError(
ValueError: Bad serialized model or bad model name. There are several possible causes. If you are using a DGL model, you need to set the backend to DGL using `matgl.set_backend('DGL')`. If you have an outdated cached model, please 'clear your cache by running `python -c 'import matgl; matgl.clear_cache()'`
