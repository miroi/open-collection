================
ASE-driven DIRAC
================

installation
------------

(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/.pip install -e .
Obtaining file:///home/miroi/work/software/dirac/trunk_cloned/ase_dirac
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: ase in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase_dirac==1.0.0) (3.28.0b1)
Requirement already satisfied: numpy>=1.21.6 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (1.26.4)
Requirement already satisfied: scipy>=1.8.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (1.16.0)
Requirement already satisfied: matplotlib>=3.5.2 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (3.10.3)
Requirement already satisfied: contourpy>=1.0.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.3.2)
Requirement already satisfied: cycler>=0.10 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (4.58.5)
Requirement already satisfied: kiwisolver>=1.3.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.4.8)
Requirement already satisfied: packaging>=20.0 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (25.0)
Requirement already satisfied: pillow>=8 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (11.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (2.4.7)
Requirement already satisfied: python-dateutil>=2.7 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.17.0)
Building wheels for collected packages: ase_dirac
  Building editable for ase_dirac (pyproject.toml) ... done
  Created wheel for ase_dirac: filename=ase_dirac-1.0.0-0.editable-py3-none-any.whl size=3313 sha256=3a766cd787ab683c5b2b3cfbe95a0210f86cbdc2919e7850733e0566f7801f38
  Stored in directory: /tmp/pip-ephem-wheel-cache-2n0ds48a/wheels/df/dc/f5/947c96d9b3c3c1a56ed5c7d6f05a126679059f3098b24eb676
Successfully built ase_dirac
Installing collected packages: ase_dirac
Successfully installed ase_dirac-1.0.0

(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/.pip show ase_dirac
Name: ase_dirac
Version: 1.0.0
Summary: DIRAC ASE calculator
Home-page:
Author: Carlos M. R. Rocha
Author-email: c.rocha@esciencecenter.nl
License: Apache-2.0
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Editable project location: /home/miroi/work/software/dirac/trunk_cloned/ase_dirac
Requires: ase
Required-by:


