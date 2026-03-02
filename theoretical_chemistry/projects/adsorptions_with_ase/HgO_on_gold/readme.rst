========
HgO@Gold
========


Google AI: ase chgnet HgO adsorption energy on gold slab write python code

plus fixes

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/HgO_on_gold/.python code.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
CHGNet will run on cpu
Relaxing Gold Slab...
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1599: RuntimeWarning: divide by zero encountered in scalar divide
  x = 1.0 - distance / D_len[0]
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1608: RuntimeWarning: invalid value encountered in multiply
  R[a0] += (x * fix) * D[0]
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1610: RuntimeWarning: invalid value encountered in multiply
  R[i] -= (x * (1.0 - fix)) * D[0]
Relaxing HgO Molecule...
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Relaxing Adsorbed System...

==============================
Adsorption Energy: -1.7705 eV
==============================
Adsorption is EXOTHERMIC (stable).


ORIENTATION
===========

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/HgO_on_gold/.python orientation.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
CHGNet will run on cpu
Relaxing Au(111) Slab...
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1599: RuntimeWarning: divide by zero encountered in scalar divide
  x = 1.0 - distance / D_len[0]
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1608: RuntimeWarning: invalid value encountered in multiply
  R[a0] += (x * fix) * D[0]
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/atoms.py:1610: RuntimeWarning: invalid value encountered in multiply
  R[i] -= (x * (1.0 - fix)) * D[0]
Relaxing Isolated HgO...
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 2 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Relaxing System (Mercury-down)...
Relaxing System (Oxygen-down)...

========================================
Orientation          | Adsorption Energy (eV)
---------------------------------------------
Mercury-down         |            -1.7693 eV
Oxygen-down          |            -3.2823 eV
========================================
The most stable configuration is: Oxygen-down

MULTI-ORIENTATION
=================
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/HgO_on_gold/.python multi-orientation.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
CHGNet will run on cpu
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
/home/miroi/work/software/myenv/lib/python3.12/site-packages/ase/io/extxyz.py:320: UserWarning: Skipping unhashable information adsorbate_info
  warnings.warn('Skipping unhashable information '

Site       | Orientation  | E_ads (eV)
----------------------------------------
ontop      | Hg-down      |    -0.4891
ontop      | O-down       |    -1.2263
bridge     | Hg-down      |    -0.3541
bridge     | O-down       |    -1.6787
fcc        | Hg-down      |    -0.3114
fcc        | O-down       |    -1.6799
hcp        | Hg-down      |    -0.3085
hcp        | O-down       |    -1.6441
----------------------------------------
Most Stable: fcc / O-down (-1.6799 eV)
Check fcc_O-down_relaxed.xyz for the geometry.


predicted -1.5eV to -2 eV


