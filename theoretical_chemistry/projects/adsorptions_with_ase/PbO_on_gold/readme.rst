PbO@Au(111)
===========

from https://github.com/A-H-Hanafy/Python-Based-Fast-Screening-of-Molecular-Adsorption-Sites-on-Gold-Surfaces/tree/main/PbO%20on%20Au(111)%20Surface

(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/PbO_on_gold/.python PbO_gold111_V2.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cuda
CHGNet will run on cuda
/home/milias/work/software/venv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
The lattice constant a =  4.170014375971122
The Energy of Gold Surface Au(111) =  -150.4148
The Energy of PbO (Isolated) =  -8.688826

Site       | Orientation  | E_total (eV) | E_ads (eV)
--------------------------------------------------
ontop      | Flat         |  -160.2492 |    -1.1456
bridge     | Flat         |  -160.2511 |    -1.1474
fcc        | Flat         |  -160.2109 |    -1.1073
hcp        | Flat         |  -160.2415 |    -1.1379
----------------------------------------
Most Stable: bridge (Flat) at -1.1474 eV


(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/PbO_on_gold/.ls -lt
total 56
-rw-r--r-- 1 milias milias 6690 Mar 11 13:54 flat_hcp_relaxed.xyz
-rw-r--r-- 1 milias milias 6692 Mar 11 13:54 flat_fcc_relaxed.xyz
-rw-r--r-- 1 milias milias 6685 Mar 11 13:54 flat_bridge_relaxed.xyz
-rw-r--r-- 1 milias milias 6689 Mar 11 13:54 flat_ontop_relaxed.xyz
-rw-r--r-- 1 milias milias  481 Mar 11 13:54 isolated_pbo_relaxed.xyz
-rw-r--r-- 1 milias milias 6438 Mar 11 13:54 pure_slab_relaxed.xyz
-rw-r--r-- 1 milias milias 5567 Mar 11 13:54 PbO_gold111_V2.py
-rw-r--r-- 1 milias milias  176 Mar 11 13:53 readme.rst
