=================
Hg@C8 with CHGNet
=================

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/chgnet-ase/runs/Hg_on_C8_simple_relaxation/chgnet-calculator/.python Hg_on_C8_relaxation_chgnet.py  > Hg_on_C8_relaxation_chgnet.py_logfile
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)

Hg@C8: -73.38642311096191 eV
Hg:  0.337893 eV
C8:  -73.47447967529297 eV

Eads = Hg@C8 - C8 - Hg = -73.38642311096191 -(-73.47447967529297) - 0.337893
Eads = -0.249836435 eV


Final adsorption energy(QE):
----------------------------

Eads = E(Hg@C8)-E(C8)-E(Hg)
Eads =  -5827.982600 -( -1311.600966)-(-4516.127513)
Eads = -.254121 eV

Good AI:  Mercury's adsorption energy on pristine graphene is low (around -0.220 eV), indicating physisorption

