==========================
GPAW on WSL-Win11-VictusNB
==========================


https://wiki.fysik.dtu.dk/gpaw/install.html

sudo apt install gpaw

rather 

pip install gpaw

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/range_separated_functionals/.gpaw -P 4 test
 ----------------------------------------------------------------------------------------
| python-3.10.12    /usr/bin/python3                                                     |
| gpaw-22.1.0       /usr/lib/python3/dist-packages/gpaw/                                 |
| ase-3.23.0        /home/milias/.local/lib/python3.10/site-packages/ase/                |
| numpy-1.26.4      /home/milias/.local/lib/python3.10/site-packages/numpy/              |
| scipy-1.13.0      /home/milias/.local/lib/python3.10/site-packages/scipy/              |
| libxc-5.1.7       yes                                                                  |
| _gpaw             /usr/lib/python3/dist-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
| MPI enabled       yes                                                                  |
| OpenMP enabled    no                                                                   |
| scalapack         yes                                                                  |
| Elpa              yes; version: 20211125                                               |
| FFTW              yes                                                                  |
| libvdwxc          no                                                                   |
| PAW-datasets (1)  /usr/local/share/gpaw-setups                                         |
| PAW-datasets (2)  /usr/share/gpaw-setups                                               |
 ----------------------------------------------------------------------------------------
Doing a test calculation (cores: 4): ... Done

sudo apt remove gpaw
sudo apt purge  gpaw

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/buildup_on_servers/wsl_win11_Victus/.pip install gpaw
.
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/buildup_on_servers/wsl_win11_Victus/.pip install gpaw

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/libxc/wsl_win11_Victus/.gpaw -P 4 test
 ----------------------------------------------------------------------------------------------------------
| python-3.10.12    /usr/bin/python3                                                                       |
| gpaw-24.6.0       /home/milias/.local/lib/python3.10/site-packages/gpaw/                                 |
| ase-3.23.0        /home/milias/.local/lib/python3.10/site-packages/ase/                                  |
| numpy-1.26.4      /home/milias/.local/lib/python3.10/site-packages/numpy/                                |
| scipy-1.13.0      /home/milias/.local/lib/python3.10/site-packages/scipy/                                |
| libxc-5.1.7       yes                                                                                    |
| _gpaw             /home/milias/.local/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
| MPI enabled       yes                                                                                    |
| OpenMP enabled    no                                                                                     |
| GPU enabled       no                                                                                     |
| GPU-aware MPI     no                                                                                     |
| CUPY              /home/milias/.local/lib/python3.10/site-packages/gpaw/gpu/cpupy/__init__.py            |
| scalapack         no                                                                                     |
| Elpa              no                                                                                     |
| FFTW              no                                                                                     |
| libvdwxc          no                                                                                     |
| PAW-datasets (1)  /usr/local/share/gpaw-setups                                                           |
| PAW-datasets (2)  /usr/share/gpaw-setups                                                                 |
 ----------------------------------------------------------------------------------------------------------
Doing a test calculation (cores: 4): ... Done

