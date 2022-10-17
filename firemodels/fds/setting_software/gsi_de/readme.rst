The installation directory, /data.local1/milias/software/fds-smv, has been created.

Copying FDS installation files to /data.local1/milias/software/fds-smv
Copy complete.
Creating directory /data.local1/milias/software/fds-smv/bin/modules
The installation directory, /data.local1/milias/software/fds-smv/bin/modules, has been created.

-----------------------------------------------
*** To complete the installation:

1. Add the following lines to your startup file
   (usually /u/milias/.bashrc).

source /data.local1/milias/software/fds-smv/bin/FDS6VARS.sh
source /data.local1/milias/software/fds-smv/bin/SMV6VARS.sh

or if you are using modules, add:

export MODULEPATH=/data.local1/milias/software/fds-smv/bin/modules:$MODULEPATH
module load FDS6
module load SMV6

2. Log out and log back in so that the changes will take effect.

