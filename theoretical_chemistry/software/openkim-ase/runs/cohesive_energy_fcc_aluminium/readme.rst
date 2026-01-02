ASE-OpenKIM
============

see https://openkim.org/doc/usage/using-models for ASE

and https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html

coh_en1.py
~~~~~~~~~~

milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/openkim/buildup_on_servers/jinr_ru/wsl_win10_pc7321b/cohesive_energy_fcc_aluminium/.python3 coh_en1.py
Computed cohesive energy of 3.359 eV/atom (experiment: 3.39 eV/atom)
Computed pressure of -1049.704221612884 MPa

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/.python coh_en1.py
/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/coh_en1.py:19: FutureWarning: Please use atoms.calc = calc
  atoms.set_calculator(calc)
Computed cohesive energy of 3.359 eV/atom (experiment: 3.39 eV/atom)
Computed pressure of -1049.7042216128843 MPa

coh_en2.py
~~~~~~~~~~

milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/openkim/buildup_on_servers/jinr_ru/wsl_win10_pc7321b/cohesive_energy_fcc_aluminium/.python3 coh_en2.py

see https://matsci.org/t/typeerror-cant-multiply-sequence-by-non-int-of-type-float/56345

https://github.com/openkim/kim-query/issues/3

Fixed, https://github.com/openkim/kim-query/issues/3#issuecomment-2214565263 :

milias@pc7321b:/mnt/c/Users/milias/My Documents/git-projects/open-collection/theoretical_chemistry/software/openkim/buildup_on_servers/jinr_ru/wsl_win10_pc7321b/cohesive_energy_fcc_aluminium/.python3 coh_en2.py
doing query to get lattice constant for this model= EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005
obtained a0= 4.032082033157349
Computed cohesive energy of 3.360 eV/atom (experiment: 3.39 eV/atom)
Computed pressure of -0.0036923616494566416 MPa

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/.pip install kim_query
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/.python coh_en2.py
doing query to get lattice constant for this model= EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005
obtained a0= 4.032082033157349
/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/coh_en2.py:26: FutureWarning: Please use atoms.calc = calc
  atoms.set_calculator(calc)
Computed cohesive energy of 3.360 eV/atom (experiment: 3.39 eV/atom)
Computed pressure of -0.0036923616495188262 MPa

coh_en3.py
~~~~~~~~~~
milias@pc7321b:/mnt/c/Users/milias/My Documents/git-projects/open-collection/theoretical_chemistry/software/openkim/buildup_on_servers/jinr_ru/wsl_win10_pc7321b/cohesive_energy_fcc_aluminium/.python3 coh_en3.py > coh_en3py.logfile

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/.kim-api-collections-management install user  EAM_CubicNaturalSpline_ErcolessiAdams_1994_Al__MO_800509458712_003
.
Success!

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/cohesive_energy_fcc_aluminium/.python3 coh_en3.py
Ecoh [eV]    KIM Potential
      3.360  EAM_CubicNaturalSpline_ErcolessiAdams_1994_Al__MO_800509458712_003
unavailable  EAM_CubicNaturalSpline_ErcolessiAdams_1994_Al__MO_800509458712_003
unavailable  EAM_Dynamo_AngeloMoodyBaskes_1995_NiAlH__MO_418978237058_006
.
.


