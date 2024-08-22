OpenKIM example
===============

https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html


As an example, suppose we want to know the potential energy predicted by the example model “ex_model_Ar_P_Morse_07C” for an FCC argon lattice at a lattice spacing of 5.25 Angstroms. This can be accomplished in a manner similar to how most other ASE calculators are used, where the name of the KIM model is passed as an argument:

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/.python3 morse.py
/usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.4
  warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"
Potential energy of FCC Ar: -0.37120682093323026 eV

