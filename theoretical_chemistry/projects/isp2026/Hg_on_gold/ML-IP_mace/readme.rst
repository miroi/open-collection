Hg@Gold111
==========

AI help
--------
https://chat.deepseek.com/share/1c1xrbgq3fgcbd08lg


pip install mace-torch

fix:
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/isp2026/Hg_on_gold/ML-IP_mace/.python Hg_on_Au-slab_ML.py
/home/miroi/miniconda3/envs/mace_env/lib/python3.13/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
Using Materials Project MACE for MACECalculator with /home/miroi/.cache/mace/20231203mace128L1_epoch199model
Using float32 for MACECalculator, which is faster but less accurate. Recommended for MD. Use float64 for geometry optimization.
/home/miroi/miniconda3/envs/mace_env/lib/python3.13/site-packages/mace/calculators/mace.py:226: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  torch.load(f=model_path, map_location=device)
WARNING:root:Default dtype float32 does not match model dtype float64, converting models to float32.
Optimizing Au Slab...
Optimizing Hg + Au System...

==============================
Slab Energy:       -301.5494 eV
Hg Atom Energy:       0.0905 eV
Combined Energy:   -302.1863 eV
------------------------------
Adsorption Energy:    -0.7274 eV
==============================
