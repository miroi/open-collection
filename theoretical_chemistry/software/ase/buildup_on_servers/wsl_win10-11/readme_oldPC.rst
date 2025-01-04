=========================
MiroPhenomII-X6 Ubuntu 24
=========================

miroi@MiroPhenomII-X6:~/software/.lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.1 LTS
Release:        24.04
Codename:       noble

miroi@MiroPhenomII-X6:~/software/.source venv/bin/activate
(venv) miroi@MiroPhenomII-X6:~/software/.pip install ase
Collecting ase
  Downloading ase-3.24.0-py3-none-any.whl.metadata (3.9 kB)
Collecting numpy>=1.19.5 (from ase)
  Downloading numpy-2.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.0/62.0 kB 404.1 kB/s eta 0:00:00
Collecting scipy>=1.6.0 (from ase)
  Downloading scipy-1.14.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.8/60.8 kB 1.5 MB/s eta 0:00:00
Collecting matplotlib>=3.3.4 (from ase)
  Downloading matplotlib-3.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Collecting contourpy>=1.0.1 (from matplotlib>=3.3.4->ase)
  Downloading contourpy-1.3.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.4 kB)
Collecting cycler>=0.10 (from matplotlib>=3.3.4->ase)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib>=3.3.4->ase)
  Downloading fonttools-4.55.3-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (165 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 165.1/165.1 kB 678.3 kB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib>=3.3.4->ase)
  Downloading kiwisolver-1.4.8-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.2 kB)
Requirement already satisfied: packaging>=20.0 in ./venv/lib/python3.12/site-packages (from matplotlib>=3.3.4->ase) (24.2)
Collecting pillow>=8 (from matplotlib>=3.3.4->ase)
  Downloading pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting pyparsing>=2.3.1 (from matplotlib>=3.3.4->ase)
  Downloading pyparsing-3.2.0-py3-none-any.whl.metadata (5.0 kB)
Collecting python-dateutil>=2.7 (from matplotlib>=3.3.4->ase)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Requirement already satisfied: six>=1.5 in ./venv/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib>=3.3.4->ase) (1.17.0)
Downloading ase-3.24.0-py3-none-any.whl (2.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.9/2.9 MB 1.3 MB/s eta 0:00:00
Downloading matplotlib-3.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.6/8.6 MB 1.3 MB/s eta 0:00:00
Downloading numpy-2.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.1/16.1 MB 2.1 MB/s eta 0:00:00
Downloading scipy-1.14.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (40.8 MB)
   ━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/40.8 MB 2.1 MB/s eta 0:00:17
   ━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━ 21.0/40.8 MB 2.4 MB/s eta 0:00:09
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.8/40.8 MB 2.2 MB/s eta 0:00:00
Downloading contourpy-1.3.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (323 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 323.6/323.6 kB 2.3 MB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.55.3-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 2.5 MB/s eta 0:00:00
Downloading kiwisolver-1.4.8-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 3.0 MB/s eta 0:00:00
Downloading pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl (4.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 3.2 MB/s eta 0:00:00
Downloading pyparsing-3.2.0-py3-none-any.whl (106 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.9/106.9 kB 2.3 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 3.0 MB/s eta 0:00:00
Installing collected packages: python-dateutil, pyparsing, pillow, numpy, kiwisolver, fonttools, cycler, scipy, contourpy, matplotlib, ase

Successfully installed ase-3.24.0 contourpy-1.3.1 cycler-0.12.1 fonttools-4.55.3 kiwisolver-1.4.8 matplotlib-3.10.0 numpy-2.2.1 pillow-11.0.0 pyparsing-3.2.0 python-dateutil-2.9.0.post0 scipy-1.14.1
(venv) miroi@MiroPhenomII-X6:~/software/.

miroi@MiroPhenomII-X6:~/software/.source venv/bin/activate
(venv) miroi@MiroPhenomII-X6:~/software/.ase info
/home/miroi/software/venv/lib/python3.12/site-packages/numpy/_core/getlimits.py:551: UserWarning: Signature b'\x00\xd0\xcc\xcc\xcc\xcc\xcc\xcc\xfb\xbf\x00\x00\x00\x00\x00\x00' for <class 'numpy.longdouble'> does not match any known type: falling back to type probe function.
This warnings indicates broken support for the dtype!
  machar = _get_machar(dtype)
platform                 Linux-4.4.0-19041-Microsoft-x86_64-with-glibc2.39
python-3.12.3            /home/miroi/software/venv/bin/python3
ase-3.24.0               /home/miroi/software/venv/lib/python3.12/site-packages/ase
numpy-2.2.1              /home/miroi/software/venv/lib/python3.12/site-packages/numpy
scipy-1.14.1             /home/miroi/software/venv/lib/python3.12/site-packages/scipy
matplotlib-3.10.0        /home/miroi/software/venv/lib/python3.12/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2                 not installed
pyamg                    not installed

(venv) miroi@MiroPhenomII-X6:~/software/.sudo apt-get install python3-tk

(venv) miroi@MiroPhenomII-X6:~/software/.ase gui
/home/miroi/software/venv/lib/python3.12/site-packages/numpy/_core/getlimits.py:551: UserWarning: Signature b'\x00\xd0\xcc\xcc\xcc\xcc\xcc\xcc\xfb\xbf\x00\x00\x00\x00\x00\x00' for <class 'numpy.longdouble'> does not match any known type: falling back to type probe function.
This warnings indicates broken support for the dtype!
  machar = _get_machar(dtype)
usage: ase [-h] [--version] [-T]
           {help,info,test,gui,db,run,band-structure,build,dimensionality,eos,ulm,find,nebplot,nomad-upload,nomad-get,convert,reciprocal,completion,diff,exec}
           ...
ase: error: TclError: no display name and no $DISPLAY environment variable
To get a full traceback, use: ase -T gui ...

(venv) miroi@MiroPhenomII-X6:~/software/.ase -T gui
/home/miroi/software/venv/lib/python3.12/site-packages/numpy/_core/getlimits.py:551: UserWarning: Signature b'\x00\xd0\xcc\xcc\xcc\xcc\xcc\xcc\xfb\xbf\x00\x00\x00\x00\x00\x00' for <class 'numpy.longdouble'> does not match any known type: falling back to type probe function.
This warnings indicates broken support for the dtype!
  machar = _get_machar(dtype)
Traceback (most recent call last):
  File "/home/miroi/software/venv/bin/ase", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/cli/main.py", line 102, in main
    f(args)
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/gui/ag.py", line 106, in run
    gui = GUI(images, args.rotations, args.bonds, args.graph)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/gui/gui.py", line 45, in __init__
    self.window = ui.ASEGUIWindow(close=self.exit, menu=menu,
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/gui/ui.py", line 599, in __init__
    MainWindow.__init__(self, 'ASE-GUI', close, menu)
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/gui/ui.py", line 500, in __init__
    self.win = tk.Tk()
               ^^^^^^^
  File "/usr/lib/python3.12/tkinter/__init__.py", line 2345, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_tkinter.TclError: couldn't connect to display ":0.0"
(venv) miroi@MiroPhenomII-X6:~/software/.