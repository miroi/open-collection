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

