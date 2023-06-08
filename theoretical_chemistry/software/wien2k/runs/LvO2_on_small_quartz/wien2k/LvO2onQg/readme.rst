LvO2@smalQ-G with wien2k
=========================

setrmt_lapw@
file    LvO2onQg.struct_setrmt   generated

LvO2onQg.struct_SAVED

cp LvO2onQg.in1 LvO2onQg.in1c
cp LvO2onQg.in2 LvO2onQg.in2c

milias@adf2:~/work/projects/open-collection/theoretical_chemistry/software/wien2k/runs/LvO2_on_small_quartz/wien2k/LvO2onQg/.pu | grep 'nlvdw'
User processes: 
milias    5296  5294  0 21:05 ?        00:00:00 /bin/tcsh -f ./run_lapw -nlvdw -ec 0.0001 -NI
milias    5323  5296  0 21:05 ?        00:00:00 /bin/tcsh -f ./x nlvdw
milias    5337  5323 99 21:05 ?        00:01:09 ./nlvdw nlvdw.def


Formatted files for dstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
'LvO2onQg.in0','old',    'formatted',0
'LvO2onQg.in2c',   'old',    'formatted',0
'LvO2onQg.in1c',   'old',    'formatted',0
'LvO2onQg.struct',      'old',    'formatted',0
'LvO2onQg.rsp',    'old',    'formatted',0

cat  lapw0.def  | grep old:
LvO2onQg.in0',     'old',    'formatted',0
LvO2onQg.clmsum',  'old',    'formatted',0
LvO2onQg.struct',  'old',    'formatted',0         
LvO2onQg.innlvdw',   'old','formatted',0

cat  lapw1.def  | grep old
'LvO2onQg.in1c',   'old',    'formatted',-1
'LvO2onQg.vsp',       'old',    'formatted',-1
'LvO2onQg.struct',         'old',    'formatted',-1





./run_lapw -nlvdw -ec 0.0001 -NI


