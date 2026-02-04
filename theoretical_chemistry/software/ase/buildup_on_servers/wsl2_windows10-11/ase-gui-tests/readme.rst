=======================
ase gui on WLS-Win10/11
=======================

see https://gitlab.com/ase/ase/-/issues/1511

via venv
---------
milias@pc7321b:~/.source ~/work/venv/bin/activate
(venv) milias@pc7321b:~/.deactivate
milias@pc7321b:~/.

the problem remains  https://gitlab.com/ase/ase/-/issues/1511


(venv) milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/wsl_win10-11/ase-gui-tests/.sudo apt-get remove python3-tk

(venv) milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/wsl_win10-11/ase-gui-tests/.ase gui
usage: ase [-h] [--version] [-T]
           {help,info,test,gui,db,run,band-structure,build,dimensionality,eos,ulm,find,nebplot,nomad-upload,nomad-get,convert,reciprocal,completion,diff,exec} ...
ase: error: ModuleNotFoundError: No module named 'tkinter'
To get a full traceback, use: ase -T gui ...

(venv) milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/wsl_win10-11/ase-gui-tests/.pip3 install tk
Collecting tk
  Downloading tk-0.1.0-py3-none-any.whl (3.9 kB)
Installing collected packages: tk
Successfully installed tk-0.1.0

python3 tkinter_test.py ... this works...

solution
~~~~~~~~
clean all the pip packages, use sudo replacements for missing

pip install ase_ext
pip install asap3


