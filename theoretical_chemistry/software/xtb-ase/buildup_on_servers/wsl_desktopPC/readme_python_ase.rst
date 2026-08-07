xtb-python installation
========================

based on https://xtb-python.readthedocs.io/en/latest/installation.html#building

git clone https://github.com/grimme-lab/xtb-python
pip install meson
pip install cffi nija qcelemental


milias@DESKTOP-7OTLCGO:~/work/software/xtb/xtb-python/.sudo apt install intel-mkl  (no default )

milias@DESKTOP-7OTLCGO:~/work/software/xtb/xtb-python/.pip install .
.
.
      ../meson.build:77:16: ERROR: Command `/usr/bin/python3 /home/milias/work/software/xtb/xtb-python/ffibuilder.py /home/milias/work/software/xtb/xtb-python/.mesonpy-ta1g4_6x/_libxtb.h _libxtb` failed with status 1.

      A full log can be found at /home/milias/work/software/xtb/xtb-python/.mesonpy-ta1g4_6x/meson-logs/meson-log.txt
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed
