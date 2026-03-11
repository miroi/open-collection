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

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/PbO_on_gold/abdelrham/.python   PbO_gold111_V2_03.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
CHGNet will run on cpu
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Optimized lattice constant a = 4.1700

Site     | Theta  | Phi    | E_ads
----------------------------------------
ontop    | 0      | 0      |    -0.3115
ontop    | 0      | 90     |    -0.3115
ontop    | 0      | 180    |    -0.3115
ontop    | 0      | 270    |    -0.3115
ontop    | 90     | 0      |    -1.0637
ontop    | 90     | 90     |    -0.9551
ontop    | 90     | 180    |    -1.0642
ontop    | 90     | 270    |    -0.9516
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
ontop    | 180    | 0      |    83.6699
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
ontop    | 180    | 90     |    83.6699
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
ontop    | 180    | 180    |    83.6699
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Structure graph_id=None has 34 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
ontop    | 180    | 270    |    83.6699
bridge   | 0      | 0      |    -0.3960
bridge   | 0      | 90     |    -0.3960
.
.

