======================
nwchem on WSL-Notebook
======================

sudo apt install debichem-molecular-modelling

dpkg -S nwchem   | less

milias@Miro:~/.apt-cache policy nwchem  nwchem-data
nwchem:
  Installed: 7.0.2-3

see https://github.com/nwchemgit/nwchem/releases


testing
~~~~~~~
ls /usr/share/doc/nwchem/examples/
ls  /usr/share/nwchem/
