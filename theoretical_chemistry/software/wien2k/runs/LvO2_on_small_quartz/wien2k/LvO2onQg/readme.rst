=========================
LvO2@smalQ-G with wien2k
=========================

RMT
---
O  1.05
Si 1.49 ---> 1.80 due to charge leak
H  0.57
Lv 2.20

RKMax=3.0 because of H
GMAX = 20

setrmt_lapw@
file   LvO2onQg.struct_setrmt   generated

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


Help:
https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22540.html

https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22588.html
In $WIENROOT/WIEN2k_parallel_options : if ( ! $?USE_REMOTE ) setenv USE_REMOTE 0 

dstart.def: LvO2onQg.in0  LvO2onQg.in2c  LvO2onQg.in1c LvO2onQg.struct LvO2onQg.rsp

STOP  LAPW0 END  LvO2onQg.in0  LvO2onQg.clmsum  LvO2onQg.struct
STOP  LAPW1 END  LvO2onQg.in1c  LvO2onQg.vsp 
STOP  LAPW2 END  LvO2onQg.in2c
STOP  CORE  END
STOP  MIXER END  LvO2onQg.inm LvO2onQg.clmsum_old 

error:

