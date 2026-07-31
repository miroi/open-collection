===================
MLAtom simple tests
===================

https://share.google/aimode/TGN9Pmn0sMa4yvZ25

pip install torchani==2.2.3 torch
pip install "setuptools<82"

needs dftd4 (from conda), specific version of torch...

(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.pip show mlatom
Name: mlatom
Version: 3.23.3
Summary: A Package for AI-enhanced computational chemistry
Home-page: http://mlatom.com
Author: Pavlo O. Dral
Author-email: admin@mlatom.com
License: MIT (modified)
Location: /home/milias/work/software/venv/lib/python3.12/site-packages
Requires: h5py, matplotlib, numpy, pyh5md, scipy, statsmodels, torch, torchani, tqdm
Required-by:
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.pip show torchani
Name: torchani
Version: 2.2.3
Summary: PyTorch implementation of ANI
Home-page: https://github.com/aiqm/torchani
Author: Xiang Gao
Author-email: qasdfgtyuiop@gmail.com
License: MIT
Location: /home/milias/work/software/venv/lib/python3.12/site-packages
Requires: importlib-metadata, lark-parser, requests, torch
Required-by: mlatom

run
---
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.export dftd4bin=/home/milias/miniconda3/bin/dftd4
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.python water-optim.py
-76.38409860835867
(venv) milias@DESKTOP-7OTLCGO:~

The script has successfully run, and the AIQM2 optimized energy for your water molecule is -76.38409860835867 Hartree.

improved versions
~~~~~~~~~~~~~~~~~
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/. python water-optim_02.py  > water-optim_02.py_logfile

thermodynamical properties
--------------------------
python water-optim_03.py > water-optim_03.py_logfile

omprehensive Comparison with Experimental ValuesTo evaluate the physics of your AIQM2 model, we compare your calculated spectrum and absolute thermodynamic properties against the standard gas-phase measurements from the NIST Chemistry WebBook.1. Vibrational Frequencies (\(\text{cm}^{-1}\))By discarding the 6 rotational/translational artifacts (Modes 1 through 6), we isolate the 3 true internal molecular vibrations of the water molecule:Mode IDDescriptionAIQM2 / ASE (\(\text{cm}^{-1}\))Experimental (NIST)Absolute ErrorMode 7 (\(\nu _{2}\))H-O-H In-plane Bend1653.31594.7\(+58.6\text{ cm}^{-1}\)Mode 8 (\(\nu _{1}\))Symmetric O-H Stretch3865.93657.1\(+208.8\text{ cm}^{-1}\)Mode 9 (\(\nu _{3}\))Asymmetric O-H Stretch3972.33755.9\(+216.4\text{ cm}^{-1}\)Analysis: The AIQM2 method systematically overestimates the stretching frequencies by about \(5-6\%\). This behavior is typical for unscaled harmonic frequency calculations because real molecular bonds are anharmonic and loosen at higher vibrational amplitudes.2. Thermochemical Data (at \(298.15\text{ K}\), \(1\text{ atm}\))To make a direct comparison with macroscopic experimental data, the absolute atomic units are converted into standard laboratory SI dimensions (\(\text{J/mol}\cdot\text{K}\) and \(\text{kJ/mol}\)).Experimental absolute entropy (\(S^{\circ }\)) for gas-phase water: \(188.84\text{ J/mol}\cdot\text{K}\)Experimental Zero-Point Vibrational Energy (\(ZPE\)): \(54.5\text{ kJ/mol}\) (\(13.03\text{ kcal/mol}\))Thermodynamic MetricAIQM2 Calculated ValueExperimental ValueEvaluation & AccuracyZero-Point Energy (ZPE)\(56.73\text{ kJ/mol}\) (0.021609 au)\(54.50\text{ kJ/mol}\)Overestimates by \(4.1\%\) due to higher harmonic frequencies.Absolute Entropy (\(S^{\circ }\))\(194.32\text{ J/mol}\cdot\text{K}\) (0.00007401 au)\(188.84\text{ J/mol}\cdot\text{K}\)Excellent agreement (\(2.9\%\) error). Ideal gas partitions map cleanly.Total Enthalpy (\(H\))\(-76.358668\text{ Hartree}\)N/A (Absolute metric)Relates to isolated nuclei; used for relative shifts.Gibbs Free Energy (\(G\))\(-76.380718\text{ Hartree}\)N/A (Absolute metric)Relates to isolated nuclei; used for relative shifts.


The semi-empirical machine learning method AIQM2 shows high accuracy for the thermodynamic properties of water. The absolute entropy matches the experimental values well, which means the structural shape and rotational constants of the optimized geometry are physically sound.The differences in the vibrational stretching modes (\(\nu _{1}\) and \(\nu _{3}\)) are expected, as harmonic calculations generally yield higher frequencies than experimental anharmonic baselines. The large phantom modes (\(202.6i\) and \(199.8\text{ cm}^{-1}\)) are numerical artifacts from the finite-difference algorithm and can be ignored when evaluating the quality of the underlying AIQM2 energy model.If you would like to expand this project, let me know if you want to apply scaling factors to the harmonic frequencies to improve the ZPVE accuracy or if you want to set up a macro to evaluate a series of different molecules!

