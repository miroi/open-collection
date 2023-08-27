===============
Phonos with ASE
===============

https://wiki.fysik.dtu.dk/ase/ase/phonons.html

see https://listserv.fysik.dtu.dk/pipermail/ase-users/2020-September/005656.html

adf2
----
python3 yum install eog 
eog Al_phonon.png 

devana_nscc_sk
--------------
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/phonons/.python3 phonon_Al_bulk.py 
<ase.phonons.Phonons object at 0x2ba93b8a9070>
WARNING, 3 imaginary frequencies at q = ( 0.00,  0.00,  0.00) ; (omega_q = 1.035e-08*i)
WARNING, 3 imaginary frequencies at q = ( 0.00,  0.00,  0.00) ; (omega_q = 1.035e-08*i)
Traceback (most recent call last):
  File "/home/milias/work/projects/open-collection/theoretical_chemistry/software/ase/runs/phonons/phonon_Al_bulk.py", line 37, in <module>
    dosax.fill_between(dos.weights[0], dos.energy, y2=0, color='grey',
AttributeError: 'GridDOSData' object has no attribute 'weights'

