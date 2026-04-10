chgnet

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/Hg_on_gold/ML-IP_chgnet/.python Hg_on_Au-slab_chgnet.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
Optimizing clean Au slab...
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Calculating isolated Hg atom energy...
Structure graph_id=None has 1 isolated atom(s) with atom_graph_cutoff=6. CHGNet calculation will likely go wrong
Optimizing Hg at fcc site...
Optimizing Hg at ontop site...

========================================
Site       | E_total (eV)    | E_ads (eV)
----------------------------------------
fcc        | Done            |    -0.8986 eV
ontop      | Done            |    -0.7069 eV
========================================
Note: A negative E_ads indicates stable adsorption.


