=========================
LvO2@smalQ-G with wien2k
=========================

No ssh on lxir127
----------------
WIENROOT=/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl

https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22588.html
In $WIENROOT/WIEN2k_parallel_options : if ( ! $?USE_REMOTE ) setenv USE_REMOTE 0 

RMT
---
O  1.05
Si 1.49 ---> 1.80 due to charge leak
H  0.57
Lv 2.20

RKMax=3.0 because of H
GMAX = 20


Files
-----
milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.cfc0c.5120/LvO2onQg/.ls
dstart.def     lapw2_7.error       LvO2onQg.clmsum_old  LvO2onQg.energydn_1  LvO2onQg.output1_3   LvO2onQg.scf1_3      LvO2onQg.vrespdn
dstart.error   lapw2_8.def         LvO2onQg.clmup       LvO2onQg.energydn_2  LvO2onQg.output1_4   LvO2onQg.scf1_4      LvO2onQg.vrespsum
lapw0.def      lapw2_8.error       LvO2onQg.clmval      LvO2onQg.energydn_3  LvO2onQg.output1_5   LvO2onQg.scf1_5      LvO2onQg.vrespsum_old
lapw0.error    lapw2.def           LvO2onQg.clmval_1    LvO2onQg.energydn_4  LvO2onQg.output1_6   LvO2onQg.scf1_6      LvO2onQg.vrespup
lapw1_1.def    lapw2.error         LvO2onQg.clmval_2    LvO2onQg.energydn_5  LvO2onQg.output1_7   LvO2onQg.scf1_7      LvO2onQg.vsp
lapw1_1.error  lcore.def           LvO2onQg.clmval_3    LvO2onQg.energydn_6  LvO2onQg.output1_8   LvO2onQg.scf1_8      LvO2onQg.vspdn
lapw1_2.def    lcore.error         LvO2onQg.clmval_4    LvO2onQg.energydn_7  LvO2onQg.output2     LvO2onQg.scf2        LvO2onQg.vsp_old
lapw1_2.error  :log                LvO2onQg.clmval_5    LvO2onQg.energydn_8  LvO2onQg.output2_1   LvO2onQg.scf2_1      LvO2onQg.vtaudn
lapw1_3.def    LvO2onQg.broyd1     LvO2onQg.clmval_6    LvO2onQg.grr         LvO2onQg.output2_2   LvO2onQg.scf2_2      LvO2onQg.vtotal
lapw1_3.error  LvO2onQg.broyd2     LvO2onQg.clmval_7    LvO2onQg.in0         LvO2onQg.output2_3   LvO2onQg.scf2_3      LvO2onQg.weight
lapw1_4.def    LvO2onQg.broyd2015  LvO2onQg.clmval_8    LvO2onQg.in0abp      LvO2onQg.output2_4   LvO2onQg.scf2_4      LvO2onQg.weight_1
lapw1_4.error  LvO2onQg.broyd2016  LvO2onQg.corewf      LvO2onQg.in0_std     LvO2onQg.output2_5   LvO2onQg.scf2_5      LvO2onQg.weight_2
lapw1_5.def    LvO2onQg.broyd2017  LvO2onQg.dayfile     LvO2onQg.in1c        LvO2onQg.output2_6   LvO2onQg.scf2_6      LvO2onQg.weight_3
lapw1_5.error  LvO2onQg.broyd2018  LvO2onQg.dmat        LvO2onQg.in2c        LvO2onQg.output2_7   LvO2onQg.scf2_7      LvO2onQg.weight_4
lapw1_6.def    LvO2onQg.broyd2019  LvO2onQg.dmat_1      LvO2onQg.inc         LvO2onQg.output2_8   LvO2onQg.scf2_8      LvO2onQg.weight_5
lapw1_6.error  LvO2onQg.broyd2020  LvO2onQg.dmat_2      LvO2onQg.indstart    LvO2onQg.outputc     LvO2onQg.scf2p       LvO2onQg.weight_6
lapw1_7.def    LvO2onQg.broyd2021  LvO2onQg.dmat_3      LvO2onQg.inm         LvO2onQg.outputd     LvO2onQg.scfc        LvO2onQg.weight_7
lapw1_7.error  LvO2onQg.broyd2022  LvO2onQg.dmat_4      LvO2onQg.inso        LvO2onQg.outputm     LvO2onQg.scfdm       LvO2onQg.weight_8
lapw1_8.def    LvO2onQg.broyd2023  LvO2onQg.dmat_5      LvO2onQg.kgen        LvO2onQg.outputsum   LvO2onQg.scfm        LvO2onQg.weightaver
lapw1_8.error  LvO2onQg.broyd2024  LvO2onQg.dmat_6      LvO2onQg.klist       LvO2onQg.qdmft       LvO2onQg.struct      LvO2onQg.weightdn
lapw1.def      LvO2onQg.broyd2025  LvO2onQg.dmat_7      LvO2onQg.klist_1     LvO2onQg.qtl         LvO2onQg.taucor      LvO2onQg.weightdn_1
lapw1.error    LvO2onQg.broyd2026  LvO2onQg.dmat_8      LvO2onQg.klist_2     LvO2onQg.r2v         LvO2onQg.taucordn    LvO2onQg.weightdn_2
lapw2_1.def    LvO2onQg.broyd2027  LvO2onQg.dmftsym     LvO2onQg.klist_3     LvO2onQg.r2v2        LvO2onQg.taudn       LvO2onQg.weightdn_3
lapw2_1.error  LvO2onQg.broyd2028  LvO2onQg.eecedn      LvO2onQg.klist_4     LvO2onQg.r2v_nonloc  LvO2onQg.tausum      LvO2onQg.weightdn_4
lapw2_2.def    LvO2onQg.broyd2029  LvO2onQg.eeceup      LvO2onQg.klist_5     LvO2onQg.radwf       LvO2onQg.tausum_old  LvO2onQg.weightdn_5
lapw2_2.error  LvO2onQg.broyd2030  LvO2onQg.energy      LvO2onQg.klist_6     LvO2onQg.recprlist   LvO2onQg.tauup       LvO2onQg.weightdn_6
lapw2_3.def    LvO2onQg.broyd2031  LvO2onQg.energy_1    LvO2onQg.klist_7     LvO2onQg.rhopw       LvO2onQg.test        LvO2onQg.weightdn_7
lapw2_3.error  LvO2onQg.broyd2032  LvO2onQg.energy_2    LvO2onQg.klist_8     LvO2onQg.rotlm       LvO2onQg.vcoul       LvO2onQg.weightdn_8
lapw2_4.def    LvO2onQg.broyd2033  LvO2onQg.energy_3    LvO2onQg.lcorepot    LvO2onQg.rsp         LvO2onQg.vec         mixer.def
lapw2_4.error  LvO2onQg.broyd2034  LvO2onQg.energy_4    LvO2onQg.mbjmix      LvO2onQg.rsplcore    LvO2onQg.vlapldn     mixer.error
lapw2_5.def    LvO2onQg.clmcor     LvO2onQg.energy_5    LvO2onQg.nsh         LvO2onQg.scf         LvO2onQg.vns         :parallel
lapw2_5.error  LvO2onQg.clmcordn   LvO2onQg.energy_6    LvO2onQg.oubwin      LvO2onQg.scf0        LvO2onQg.vnsdn       :parallel_dstart
lapw2_6.def    LvO2onQg.clmdn      LvO2onQg.energy_7    LvO2onQg.output0     LvO2onQg.scf1        LvO2onQg.vns_old     :parallel_lapw0
lapw2_6.error  LvO2onQg.clmsc      LvO2onQg.energy_8    LvO2onQg.output1_1   LvO2onQg.scf1_1      LvO2onQg.vorb        sumpara.def
lapw2_7.def    LvO2onQg.clmsum     LvO2onQg.energydn    LvO2onQg.output1_2   LvO2onQg.scf1_2      LvO2onQg.vorbup      sumpara.error

milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.cfc0c.5120/LvO2onQg/.grep ':ENE' *.out*
LvO2onQg.outputm::ENE  : ********** TOTAL ENERGY IN Ry =      -107975.12292269

