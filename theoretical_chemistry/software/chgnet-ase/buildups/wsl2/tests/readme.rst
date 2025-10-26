===========
Simple test
===========

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/.python test.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cuda
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
CHGNet-predicted energy (eV/atom):
-7.367691516876221

CHGNet-predicted forces (eV/A):
[[ 2.9802322e-08 -8.0093741e-08  2.3816191e-02]
 [-1.0430813e-07 -1.2584496e-07 -2.3816586e-02]
 [-1.4901161e-07  1.5087426e-07  9.2586935e-02]
 [ 5.9604645e-08 -7.4505806e-09 -9.2585765e-02]
 [ 2.9802322e-07  4.0046871e-08 -2.4346411e-03]
 [ 2.0861626e-07 -4.0670857e-06 -1.3071477e-02]
 [-1.7881393e-07  3.9092265e-06  1.3071299e-02]
 [-0.0000000e+00  1.1269003e-07  2.4342760e-03]]

CHGNet-predicted stress (GPa):
[[-3.0424166e-01  3.1903298e-06  7.0658541e-07]
 [ 2.7110141e-06  2.2296466e-01  6.7775352e-07]
 [-6.1479085e-08  2.6895809e-06 -1.0732203e-01]]

CHGNet-predicted magmom (mu_B):
[3.0492842e-03 3.0492246e-03 3.8694177e+00 3.8694177e+00 4.4135690e-02
 3.8622081e-02 3.8622081e-02 4.4135630e-02]


