================
AERMET pre Salem
================

Potrebujeme subory:

stage1.inp
stage2.inp
stage3.inp
.
.
.



Spustenie generovania suborov:

copy stage1.inp aermet.inp
aermet.exe    # z 24232_85_91.ua (upperair) a salem.txt (surface)  vytvori SAMEL.IQA, SALEM.OQA-surface;UPPER.IQA,UPPER.OQA -upper air
copy stage2.inp aermet.inp
aermet.exe # z UPPER.OQA a SALEM.OQA vyrobi SALEM.MET
copy stage3.inp aermet.inp
aermet.exe # zo SALEM.MET vytvori salem_86-90.sfc a salem_86-90.pfl

Na zaver teda  ziskam klucove vstupne subory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SALEM_86-90.PFL
SALEM_86-90.SFC

