Og solid melting
================

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/Og_solid/melting/.source ~/work/software/venv/bin/activate

pip install asap3
.
.
  Running setup.py install for asap3 ... done
Successfully installed asap3-3.13.6

(venv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/Og_solid/melting/.python3 melting.py  > melting.log

MiroPhenomII-X6
---------------
see https://matsci.org/t/error-in-installing-kim-model/66712/10?u=miroslav_ilias

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_tests/Og_solid/melting/.kim-api-collections-management install user LJ_ElliottAkerson_2015_Universal__MO_959249795837_003
Downloading.............. LJ_ElliottAkerson_2015_Universal__MO_959249795837_003
This item needs its driver 'LJ__MD_414112407348_003', but it is not currently installed.
Trying to find it at openkim.org.
Downloading.............. LJ__MD_414112407348_003
[100%] Built target LJ__MD_414112407348_003
Install the project...
-- Install configuration: "Release"
-- Installing: /home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/model-drivers-dir/LJ__MD_414112407348_003/libkim-api-model-driver.so
-- Set non-toolchain portion of runtime path of "/home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/model-drivers-dir/LJ__MD_414112407348_003/libkim-api-model-driver.so" to ""
[100%] Built target LJ_ElliottAkerson_2015_Universal__MO_959249795837_003
Install the project...
-- Install configuration: "Release"
-- Installing: /home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/portable-models-dir/LJ_ElliottAkerson_2015_Universal__MO_959249795837_003/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/portable-models-dir/LJ_ElliottAkerson_2015_Universal__MO_959249795837_003/libkim-api-portable-model.so" to ""

Success!

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_tests/Og_solid/melting/.python melting_Og_fcc.py
Using Asap-optimized C++-Langevin algorithm
/home/miroi/software/venv/lib/python3.12/site-packages/ase/md/md.py:54: FutureWarning: Specify the temperature in K using the 'temperature_K' argument
  warnings.warn(FutureWarning(w))
E_total = -0.09979    T = 42 K  (goal: 250 K, step 0 of 100)
E_total = -0.09491    T = 56 K  (goal: 250 K, step 1 of 100)
E_total = -0.09011    T = 84 K  (goal: 250 K, step 2 of 100)
E_total = -0.08665    T = 103 K  (goal: 250 K, step 3 of 100)
E_total = -0.08401    T = 115 K  (goal: 250 K, step 4 of 100)
E_total = -0.08101    T = 133 K  (goal: 250 K, step 5 of 100)
E_total = -0.07793    T = 146 K  (goal: 250 K, step 6 of 100)
.
.
.
