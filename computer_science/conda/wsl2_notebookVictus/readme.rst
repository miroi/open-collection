=========
miniconda 
=========

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

not adding to ~/.bashrc !!!

introduce own alias:

miroi@MIRO:~/.alias con
alias con='source /home/miroi/miniconda3/etc/profile.d/conda.sh; echo -e "miniconda activated :\c"; conda --version'
miroi@MIRO:~/.con
miniconda activated :conda 26.5.3

list of conda environments:
~~~~~~~~~~~~~~~~~~~~~~~~~~

miroi@MIRO:~/.conda env list

# conda environments:
#
# * -> active
# + -> frozen
base                     /home/miroi/miniconda3
xtb_env                  /home/miroi/miniconda3/envs/xtb_env



cleaning space
~~~~~~~~~~~~~~
miroi@MIRO:~/.conda clean --all
There are no unused tarball(s) to remove.
There are no index cache(s) to remove.
There are no unused package(s) to remove.
There are no tempfile(s) to remove.
There are no logfile(s) to remove.

conda info
~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/computer_science/conda/wsl2_notebookVictus/.conda info > conda_info.logfile


