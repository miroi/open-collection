==========================
GPAW on WSL-Win11-VictusNB
==========================


https://wiki.fysik.dtu.dk/gpaw/install.html

sudo apt-get install libopenmpi3
sudo apt-get install liblapack3 libblas3 liblapack-dev
sudo apt-get install  libopenmpi-dev
sudo apt-get install libfftw3-mpi-dev  libfftw3-mpi3 libelpa-dev
sudo apt-get install libpq-dev  libpkgconf-dev
sudo apt install meson
sudo apt-get remove meson

sudo apt install cmake

pip install meson
pip install ninja
pip install pkgconfig

pip install gpaw
pip uninstall gpaw


Only manual installation ensures proper linking against MPI, Elpa, FFTW ...

gpaw info
 ---------------------------------------------------------------------------------------------------------
| python-3.10.12    /usr/bin/python3                                                                      |
| gpaw-24.6.0       /home/miroi/.local/lib/python3.10/site-packages/gpaw/                                 |
| ase-3.23.0        /home/miroi/.local/lib/python3.10/site-packages/ase/                                  |
| numpy-1.26.4      /home/miroi/.local/lib/python3.10/site-packages/numpy/                                |
| scipy-1.14.1      /home/miroi/.local/lib/python3.10/site-packages/scipy/                                |
| libxc-5.1.7       yes                                                                                   |
| _gpaw             /home/miroi/.local/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
| MPI enabled       no                                                                                    |
| OpenMP enabled    no                                                                                    |
| GPU enabled       no                                                                                    |
| GPU-aware MPI     no                                                                                    |
| CUPY              /home/miroi/.local/lib/python3.10/site-packages/gpaw/gpu/cpupy/__init__.py            |
| scalapack         no (MPI unavailable)                                                                  |
| Elpa              no (MPI unavailable)                                                                  |
| FFTW              no                                                                                    |
| libvdwxc          no                                                                                    |
| PAW-datasets (1)  /usr/local/share/gpaw-setups                                                          |
| PAW-datasets (2)  /usr/share/gpaw-setups                                                                |
 ---------------------------------------------------------------------------------------------------------
