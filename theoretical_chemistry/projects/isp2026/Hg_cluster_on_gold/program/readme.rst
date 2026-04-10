==========================
Hg_cluster on Gold surface
==========================


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/isp2026/Hg_cluster_on_gold/program/.python adsorp_en.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
Optimizing cluster_iso...
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Optimizing slab_clean...
Optimizing total_system...
------------------------------
E_total:    -155.6909 eV
E_slab:     -150.2993 eV
E_cluster:    -2.7192 eV
Adsorption Energy:    -2.6725 eV
------------------------------
The adsorption is EXOTHERMIC (stable).
