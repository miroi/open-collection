FDS6.7.9
========

@labs.fpv.umb.sk
----------------
milias@labs.fpv.umb.sk:~/work/software/firemodels/.wget https://github.com/firemodels/fds/releases/download/FDS6.7.9/FDS6.7.9_SMV6.7.21_rls_lnx.sh
chmod u+x FDS6.7.9_SMV6.7.21_rls_lnx.sh

milias@labs.fpv.umb.sk:~/work/software/firemodels/../FDS6.7.9_SMV6.7.21_rls_lnx.sh

Options:
  Press 1 to install in /home/milias/FDS/FDS6 [default]
The installation directory, /home/milias/FDS/FDS6/bin/modules, has been created.

*** To complete the installation:

1. Add the following lines to your startup file
   (usually /home/milias/.bashrc).

source /home/milias/FDS/FDS6/bin/FDS6VARS.sh
source /home/milias/FDS/FDS6/bin/SMV6VARS.sh

or if you are using modules, add:

export MODULEPATH=/home/milias/FDS/FDS6/bin/modules:$MODULEPATH
module load FDS6
module load SMV6

@login.grid.umb.sk
------------------
1. Add the following lines to your startup file
   (usually /home/milias/.bashrc).

source /home/milias/FDS/FDS6/bin/FDS6VARS.sh
source /home/milias/FDS/FDS6/bin/SMV6VARS.sh

or if you are using modules, add:

export MODULEPATH=/home/milias/FDS/FDS6/bin/modules:$MODULEPATH
module load FDS6
module load SMV6

2. Log out and log back in so that the changes will take effect.
milias@login.grid.umb.sk:~/Work/software/.

