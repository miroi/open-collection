
AI: ASE python code for computing gold surface energy



(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/gold_surface_energy/.python vary_surface.py
Surface    | Surface Energy (eV/Å²)
----------------------------------------
(111)      | 0.032450
(100)      | 0.037615
(110)      | 0.039074

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/gold_surface_energy/.python code.py
Bulk energy per atom: 0.6512 eV
Slab energy: 4.4511 eV
Number of atoms: 36
Surface Area: 64.87 Angstrom^2
Gold (111) Surface Energy: -0.1464 eV/Angstrom^2


(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/gold_surface_energy/.python high_index_surfaces.py
Miller Index    | Surface Energy (eV/Å²)
---------------------------------------------
(2, 1, 1)       | 0.039137
(3, 2, 1)       | 0.042012
(5, 1, 1)       | 0.03950

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/gold_surface_energy/.python use_ml.py
Bulk energy per atom: 0.6512 eV
Slab energy: 4.4511 eV
Number of atoms: 36
Surface Area: 64.87 Angstrom^2
Gold (111) Surface Energy: -0.1464 eV/Angstrom^2
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Miller     | γ (eV/Å²)
-------------------------
(1, 1, 1)  | 0.011869
(1, 0, 0)  | 0.011869
(1, 1, 0)  | 0.017478
(2, 1, 1)  | 0.022249
(3, 2, 1)  | 0.029952

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/gold_surface_energy/.python surface_study.py
Bulk energy per atom: 0.6512 eV
Slab energy: 4.4511 eV
Number of atoms: 36
Surface Area: 64.87 Angstrom^2
Gold (111) Surface Energy: -0.1464 eV/Angstrom^2
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
/home/miroi/work/software/myenv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Miller Index    | γ (eV/Å²)    | Relative to (111)
--------------------------------------------------
(1, 1, 1)       | 0.011869     | 1.00
(1, 0, 0)       | 0.011869     | 1.00
(1, 1, 0)       | 0.017478     | 1.47
(2, 1, 1)       | 0.022249     | 1.87
(3, 1, 1)       | 0.025861     | 2.18
(2, 2, 1)       | 0.022055     | 1.86
(3, 2, 1)       | 0.029952     | 2.52
(5, 1, 1)       | 0.039588     | 3.34
(4, 1, 0)       | 0.037283     | 3.14
