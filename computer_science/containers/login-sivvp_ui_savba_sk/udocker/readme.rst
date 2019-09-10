udocker on login-sivvp.ui.savba.sk
==================================


udocker pull devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239

udocker run devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest bash

echo $MKLROOT  # checks MKL installation


ilias@login-sivvp.ui.savba.sk:/shared/home/ilias/Work/runs/miro_ilias_qch_systems/containers/login-sivvp.ui.savba.sk_udocker/.udocker run devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest bash
 
 ****************************************************************************** 
 *                                                                            * 
 *               STARTING 4bdb9e1f-6d94-3327-8582-f610e5d2d37f                * 
 *                                                                            * 
 ****************************************************************************** 
 executing: bash
FATAL: kernel too old

Interactive worker
------------------
qsub -I
source /shared/home/ilias/miro_ilias_bashrc/bashrc_generic
cd /shared/home/ilias/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/


udocker pull devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker images
REPOSITORY
devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:late .

Create container
~~~~~~~~~~~~~~~~
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker create --name=mirocon devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest  #
3a358e50-9dd3-3fe5-850d-7e18305ae5ae

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker ps
CONTAINER ID                         P M NAMES              IMAGE
3a358e50-9dd3-3fe5-850d-7e18305ae5ae . W ['mirocon']        devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker ps
CONTAINER ID                         P M NAMES              IMAGE
3a358e50-9dd3-3fe5-850d-7e18305ae5ae . W ['mirocon']        devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest

$ udocker run --user=root  mirocon  # FATAL: kernel too old of  3a358e50-9dd3-3fe5-850d-7e18305ae5ae !!!

Older kernel
~~~~~~~~~~~~
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker pull devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker images
REPOSITORY
devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:late .
devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest   .

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker rmi devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
Info: deleting image: devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker create --name=mirocon devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest
a8db5f91-9dbc-3789-9f32-646ccab24063
Error: invalid container name may already exist or wrong format

... better way :
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker create --name=mirocon1 devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest
efd2a9c1-8746-3151-919c-f4bdd5a939c0

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker run --user=root mirocon1
root@comp45:/home#apt-get update
root@comp45:/home#apt-get install vim
root@comp45:/home#exit

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker run --user=miro  mirocon1
Warning: non-existing user will be created

Export modified container
~~~~~~~~~~~~~~~~~~~~~~~~~
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker ps
CONTAINER ID                         P M NAMES              IMAGE
3a358e50-9dd3-3fe5-850d-7e18305ae5ae . W ['mirocon']        devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
a8db5f91-9dbc-3789-9f32-646ccab24063 . W                    devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest
efd2a9c1-8746-3151-919c-f4bdd5a939c0 . W ['mirocon1']       devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker export -o mirocon1.tar mirocon1

Import container file with image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
after deleting everything:
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker import mirocon1.tar devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest
Info: added layer 14811e0fc8fe9cbf05f07000549dec4aa960721d94c9bce42346165a1fa125e1

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker run --user=miro  mirocon1
Error: image or container not available

see https://github.com/indigo-dc/udocker/blob/master/doc/user_manual.md#62-transfer-containers-with-import

ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker import --tocontainer mirocon1.tar 
b18ccc97-3f5a-36f7-a874-6e3897cc4902
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker ps
CONTAINER ID                         P M NAMES              IMAGE
a8db5f91-9dbc-3789-9f32-646ccab24063 . W                    devcafe/cmake-cookbook_circleci_ubuntu16.04-pgi18.4:latest
b18ccc97-3f5a-36f7-a874-6e3897cc4902 . W                    IMPORTED:unknown
ilias@comp45:~/Work/runs/miro_ilias_qch_systems/containers/login-sivvp_ui_savba_sk/udocker/.udocker run --user=miro  b18ccc97-3f5a-36f7-a874-6e3897cc4902
# wooorks ! files are preserved !


