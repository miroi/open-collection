PbO@Au(111)
===========

Google AI: ASE chgnet adsorption of PbO on gold surface, all molecule orientation, code

repeating

(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/PbO_on_gold/miro/.python pbo_adsorption8.py
/home/milias/work/software/venv/lib/python3.12/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
Initializing Calculators...
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cuda
Downloading MACE model from 'https://github.com/ACEsuit/mace-mp/releases/download/mace_mp_0/2023-12-03-mace-128-L1_epoch-199.model'
Cached MACE model to /home/milias/.cache/mace/20231203mace128L1_epoch199model
Using Materials Project MACE for MACECalculator with /home/milias/.cache/mace/20231203mace128L1_epoch199model
Using float32 for MACECalculator, which is faster but less accurate. Recommended for MD. Use float64 for geometry optimization.
/home/milias/work/software/venv/lib/python3.12/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  torch.load(f=model_path, map_location=device)
WARNING:root:Default dtype float32 does not match model dtype float64, converting models to float32.

==================================================
RUNNING CALCULATOR: CHGNet
==================================================
/home/milias/work/software/venv/lib/python3.12/site-packages/chgnet/model/model.py:898: UserWarning: Converting a tensor with requires_grad=True to a scalar may lead to unexpected behavior.
Consider using tensor.detach() first. (Triggered internally at /pytorch/torch/csrc/autograd/generated/python_variable_methods.cpp:836.)
  volumes = torch.tensor(volumes, dtype=TORCH_DTYPE, device=atomic_numbers.device)
Site: ontop    | Orient: Pb-down       | E:  -122.7635 eV
Site: ontop    | Orient: O-down        | E:  -123.0329 eV
Site: ontop    | Orient: horizontal    | E:  -123.3100 eV
Site: ontop    | Orient: slant-Pb-down | E:  -122.8513 eV
Site: ontop    | Orient: slant-O-down  | E:  -123.3109 eV
Site: bridge   | Orient: Pb-down       | E:  -122.6303 eV
Site: bridge   | Orient: O-down        | E:  -123.2779 eV
Site: bridge   | Orient: horizontal    | E:  -123.4982 eV
Site: bridge   | Orient: slant-Pb-down | E:  -123.4992 eV
Site: bridge   | Orient: slant-O-down  | E:  -123.4979 eV
Site: fcc      | Orient: Pb-down       | E:  -122.7684 eV
Site: fcc      | Orient: O-down        | E:  -122.3869 eV
Site: fcc      | Orient: horizontal    | E:  -123.4871 eV
Site: fcc      | Orient: slant-Pb-down | E:  -122.7893 eV
Site: fcc      | Orient: slant-O-down  | E:  -123.2983 eV
Site: hcp      | Orient: Pb-down       | E:  -122.7709 eV
Site: hcp      | Orient: O-down        | E:  -122.3849 eV
Site: hcp      | Orient: horizontal    | E:  -123.4830 eV
Site: hcp      | Orient: slant-Pb-down | E:  -122.7481 eV
Site: hcp      | Orient: slant-O-down  | E:  -123.4864 eV

CHGNet Best: CHGNet_bridge_slant-Pb-down at -123.4992 eV

==================================================
RUNNING CALCULATOR: MACE
==================================================
Site: ontop    | Orient: Pb-down       | E:  -119.8695 eV
Site: ontop    | Orient: O-down        | E:  -120.8333 eV
Site: ontop    | Orient: horizontal    | E:  -120.7548 eV
Site: ontop    | Orient: slant-Pb-down | E:  -119.9190 eV
Site: ontop    | Orient: slant-O-down  | E:  -120.7558 eV
Site: bridge   | Orient: Pb-down       | E:  -120.0025 eV
Site: bridge   | Orient: O-down        | E:  -120.7607 eV
Site: bridge   | Orient: horizontal    | E:  -120.7226 eV
Site: bridge   | Orient: slant-Pb-down | E:  -120.0474 eV
Site: bridge   | Orient: slant-O-down  | E:  -120.7535 eV
Site: fcc      | Orient: Pb-down       | E:  -120.0366 eV
Site: fcc      | Orient: O-down        | E:  -119.6989 eV
Site: fcc      | Orient: horizontal    | E:  -120.5950 eV
Site: fcc      | Orient: slant-Pb-down | E:  -120.0605 eV
Site: fcc      | Orient: slant-O-down  | E:  -120.7574 eV
Site: hcp      | Orient: Pb-down       | E:  -120.0347 eV
Site: hcp      | Orient: O-down        | E:  -119.7009 eV
Site: hcp      | Orient: horizontal    | E:  -120.7214 eV
Site: hcp      | Orient: slant-Pb-down | E:  -120.0475 eV
Site: hcp      | Orient: slant-O-down  | E:  -120.7283 eV

MACE Best: MACE_ontop_O-down at -120.8333 eV

All results saved to 'adsorption_dual_results/'
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/PbO_on_gold/miro/.

































