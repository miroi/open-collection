===========
CHGNet test
===========

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/relaxation/.python struct_optim.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cuda
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cuda
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
      Step     Time          Energy          fmax
FIRE:    0 00:00:48      -58.941528        0.092587
CHGNet relaxed structure Full Formula (Li2 Mn2 O4)
Reduced Formula: LiMnO2
abc   :   2.868779   4.634475   5.832507
angles:  90.000000  90.000000  90.000000
pbc   :       True       True       True
Sites (8)
  #  SP      a    b         c      magmom
---  ----  ---  ---  --------  ----------
  0  Li+   0.5  0.5  0.379751  0.00304914
  1  Li+   0    0    0.62025   0.00304928
  2  Mn3+  0.5  0.5  0.863252  3.86942
  3  Mn3+  0    0    0.136747  3.86942
  4  O2-   0.5  0    0.360824  0.0441357
  5  O2-   0    0.5  0.098513  0.0386219
  6  O2-   0.5  0    0.901487  0.0386221
  7  O2-   0    0.5  0.639176  0.0441358
relaxed total energy in eV: -58.9415283203125
