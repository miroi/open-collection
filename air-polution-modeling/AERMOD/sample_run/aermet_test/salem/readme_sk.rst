================
AERMET pre Salem
================

Potrebujeme subory:

aermet.exe (executable z http://labs.fpv.umb.sk/~milias/aermod_system_execs/windows_64bit/ )

stage1.inp (vstupny subor 1)
stage2.inp (vstupny subor 2)
stage3.inp (vstupny subor 3)

24232_85_91.ua, salem.txt


Spustenie generovania suborov:

aermet.exe stage1.inp  # z 24232_85_91.ua (upperair) a salem.txt (surface)  vytvori SALEM.IQA, SALEM.OQA-surface;UPPER.IQA -upper air
aermet.exe stage2.inp  # z UPPER.OQA a SALEM.OQA vyrobi SALEM.MET
aermet.exe stage3.inp  # zo SALEM.MET vytvori salem_86-90.sfc a salem_86-90.pfl

Na zaver teda  ziskam klucove vstupne subory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SALEM_86-90.PFL
SALEM_86-90.SFC

