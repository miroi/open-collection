Simple test
===========

(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/buildups/wsl2/wsl2_win11_VictusNB/tests/.python formation_energy_CsCl.py
Do you really want to delete everything in /home/miroi/.cache/matgl (y|n)? y
MatGL pretrained models: ['CHGNet-PES-MatPES-PBE-2025.2.10', 'CHGNet-PES-MatPES-r2SCAN-2025.2.10', 'M3GNet-Eform-MP-2018.6.1', 'M3GNet-PES-ANI-1x-Subset', 'M3GNet-PES-MatPES-PBE-2025.2', 'M3GNet-PES-MatPES-r2SCAN-2025.2', 'MEGNet-BandGap-mfi-MP-2019.4.1', 'MEGNet-Eform-MP-2018.6.1', 'QET-PES-MatPES-PBE-2025.2', 'QET-PES-MatPES-r2SCAN-2025.2', 'QET-PES-MatQ', 'SO3Net-PES-ANI-1x-Subset', 'TensorNet-PES-ANI-1x-Subset', 'TensorNet-PES-MatPES-PBE-2025.2', 'TensorNet-PES-MatPES-PBE-2025.2-m', 'TensorNet-PES-MatPES-r2SCAN-2025.2', 'TensorNet-PES-MatPES-r2SCAN-2025.2-m']
model.pt: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1.13k/1.13k [00:01<00:00, 626B/s]
state.pt: 100%|████████████████████████████████████████████████████████████████████████████████████████| 796k/796k [00:02<00:00, 291kB/s]
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
model.json: 100%|███████████████████████████████████████████████████████████████████████████████████| 1.39k/1.39k [00:00<00:00, 3.79MB/s]
/home/miroi/work/software/myenv3/lib/python3.12/site-packages/matgl/utils/io.py:182: UserWarning: Incompatible model version detected! The code will continue to load the model but it is recommended that you provide a path to an updated model, increment your @model_version in model.json if you are confident that the changes are not problematic, or clear your ~/.matgl cache using `python -c "import matgl; matgl.clear_cache()"`
  _check_ver(cls_, v)  # Check version of any subclasses too.
The predicted formation energy for CsCl is -1.924 eV/atom.



