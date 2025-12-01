===========================
Hg@graphene(C8) with CHGNet
===========================

Computing adsorption energy of the Hg atom on a 8-carbon piece of graphene.

Employing CHGNet, a pretrained universal neural network potential for charge-informed atomistic modeling, see https://chgnet.lbl.gov/ .

CHGNet run
----------
python Hg_on_C8_relaxation_chgnet.py  > Hg_on_C8_relaxation_chgnet.py_logfile

getting warning:

/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)

CHGNet adsorption energy
------------------------
| Hg@C8: -73.38642311096191 eV
| Hg:   0.337893 eV
| C8:  -73.47447967529297 eV
|
Eads = Hg@C8 - C8 - Hg = -73.38642311096191 -(-73.47447967529297) - 0.337893

Eads (CHGNet) = -0.249836435 eV = -0.250 eV


Quantum Espresso (QE) adsorption energy
---------------------------------------
| Eads = E(Hg@C8)-E(C8)-E(Hg)
| Eads =  -5827.982600 -( -1311.600966)-(-4516.127513)
| Eads (QE) = -.254121 eV = -0.254 eV

Note from Google AI:
~~~~~~~~~~~~~~~~~~~~
Mercury's adsorption energy on pristine graphene is low (around -0.220 eV), indicating physisorption.

