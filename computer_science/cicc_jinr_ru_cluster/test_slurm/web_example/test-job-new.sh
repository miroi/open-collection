#!/bin/bash

# Final log file
LOGFILE=$SLURM_SUBMIT_DIR/$SLURM_JOB_ID-final.log
#Current log file
CURLOG=$TMPDIR/$SLURM_JOB_ID.log

# Redirec stdout & strerr
exec > $CURLOG 2>&1

echo “Start at: “`date`
echo “—— ARGV: 0=\”$0\” 1=\”$1\” 2=\”$2\” 3=\”$3\” 4=\”$4\””
echo “—— currunt dir”
pwd
OPWD=`pwd`
echo “—— cd $TMPDIR”
cd $TMPDIR
pwd
echo “—— hostname -f”
hostname -f
echo “—— whoami”
whoami
echo “—— id”
id
echo “—— ulimit -a”
ulimit -a
echo “—— klist”
klist
echo “—— tokens”
tokens
echo “—— eos whoami”
eos whoami
echo “—— cat $HOME/.profile >/dev/null”
cat $HOME/.profile >/dev/null
echo “—— environment”
env | grep -E “^[A-Z]” | grep -v LS_COLORS | sort
for i in `seq -w 1 3` ; do
date
echo “###################################################################### step $i”
echo “—— klist”
klist
echo “—— tokens”
tokens
echo “—— eos -b whoami”
eos -b whoami
echo “—— ps auxwww | grep -E $USER | grep -v [g]rep”
ps auxwww | grep -E “$USER” | grep -v [g]rep
echo “—— ssh -x $SLURM_SUBMIT_HOST /bin/true”
ssh -xT $SLURM_SUBMIT_HOST /bin/true
echo “—— sleep 60”
sleep 60
done
echo “Done “`date`
echo “—— rsync -aH $CURLOG $SLURM_SUBMIT_HOST:$LOGFILE-rsync”
rsync -aH $CURLOG $SLURM_SUBMIT_HOST:$LOGFILE-rsync
echo “—— cat $CURLOG | ssh -x $SLURM_SUBMIT_HOST \”cat – > $LOGFILE\””
cat $CURLOG | ssh -x $SLURM_SUBMIT_HOST “cat – > $LOGFILE”

# exit from exec
exit 0

# exit fron the job
exit 0
