VisNET
=====

pip install "mlip<=0.1.9"

pip install mlip
python -c "import mlip; print(mlip.__version__)"
0.1.9


(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/visnet-ase/buildups/wsl2/VictusNB_Win11/.python test.py
Fetching official Visnet weights from Hugging Face...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
visnet_organics_01.zip: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.59M/4.59M [00:02<00:00, 1.72MB/s]
Unpacking model structures into the execution layer...
An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.
Running simulation step via Visnet...
/home/miroi/work/software/myenv3/lib/python3.12/site-packages/ase/md/langevin.py:110: FutureWarning: The implementation of `fixcm=True` in `Langevin` does not strictly sample the correct NVT distributions. The deviations are typically small for large systems but can be more pronounced for small systems. Use `fixcm=False` together with `ase.constraints.FixCom`. `fixcm` is deprecated since ASE 3.28.0 and will be removed in a future release.
  warnings.warn(msg, FutureWarning)

--- Structural Simulation Results ---
Total Potential Energy: -4221.5425 eV

Atomic Forces (eV/Å):
[[ 0.4623125   0.6228119  -0.5776947 ]
 [-0.20814052  1.1996388   0.2615072 ]
 [-1.1542478   1.0796818   0.06452504]
 [ 1.209159   -1.0189047  -0.03248313]
 [-0.02815153 -0.6605123  -0.7966851 ]
 [ 0.08268202 -0.48349363  0.5324935 ]
 [-0.51338816 -0.30545026  0.00826572]
 [ 0.06911372 -0.41092074  0.4940296 ]
 [ 0.08066081 -0.02285092  0.04604176]]

(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/visnet-ase/buildups/wsl2/VictusNB_Win11/.python test_relax.py
Streaming genuine pre-trained Visnet weights from Hugging Face...
Download successful! Checked binary size: 0.17 MB
Loading pre-trained force field from visnet_organics.zip...
Traceback (most recent call last):
  File "/home/miroi/work/projects/open-collection/theoretical_chemistry/software/visnet-ase/buildups/wsl2/VictusNB_Win11/test_relax.py", line 34, in <module>
    force_field = load_model_from_zip(Visnet, checkpoint_filename)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/work/software/myenv3/lib/python3.12/site-packages/mlip/models/model_io.py", line 85, in load_model_from_zip
    with ZipFile(load_path, "r") as zip_object:
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/zipfile/__init__.py", line 1365, in __init__
    self._RealGetContents()
  File "/usr/lib/python3.12/zipfile/__init__.py", line 1432, in _RealGetContents
    raise BadZipFile("File is not a zip file")
zipfile.BadZipFile: File is not a zip file

downloaded files
-----------------
(myenv3) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/visnet-ase/buildups/wsl2/VictusNB_Win11/.ls -lt *.zip
-rw-r--r-- 1 miroi miroi  179474 Jun 17 01:53 visnet_organics.zip
-rw-r--r-- 1 miroi miroi 4589658 Jun 17 01:53 visnet_organics_01.zip
-rw-r--r-- 1 miroi miroi  179474 Jun 17 01:49 visnet_spice2.zip
