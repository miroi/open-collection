========================
OpenMPI on hydra.jinr.ru
========================

milias@hydra.jinr.ru:~/work/software/openmpi/.wget https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.5.tar.gz

milias@hydra.jinr.ru:~/work/software/openmpi/openmpi-5.0.5-intel_v2021.1-i8/.tar xvzf openmpi-5.0.5.tar.gz


make[4]: Entering directory `/lustre/home/user/m/milias/work/software/openmpi/openmpi-5.0.5-intel_v2021.1-i8/openmpi-5.0.5/3rd-party/prrte/src/mca/prtereachable/netlink'
  CC       reachable_netlink_module.lo
In file included from libnl_utils.h(49),
                 from reachable_netlink_module.c(27):
libnl3_utils.h(47): catastrophic error: cannot open source file "netlink/netlink.h"
  #include <netlink/netlink.h>
                              ^

compilation aborted for reachable_netlink_module.c (code 4)



