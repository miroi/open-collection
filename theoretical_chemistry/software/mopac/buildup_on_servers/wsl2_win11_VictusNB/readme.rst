MOPAC on WSL-Win11
==================

install for Linux
~~~~~~~~~~~~~~~~~~
miroi@MIRO:~/work/software/mopac/.wget http://openmopac.net/mopac-22.1.1-linux.run

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.wget https://github.com/openmopac/mopac/releases/download/v23.1.2/mopac-23.1.2-linux.run

sudo apt-get install libxcb-glx0 libxcb-glx0-dev
sudo apt-get install libx11-xcb-dev libxcb-icccm4-dev  libxcb-icccm4
sudo apt-get install libxcb-image0 libxcb-image0-dev
sudo apt-get install libxcb-keysyms1 libxcb-keysyms1-dev
sudo apt-get  libxcb-randr0  libxcb-randr0-dev
.
.
sudo apt-get install libgl-dev


miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.chmod u+x mopac-23.1.2-linux.run
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.sudo ./mopac-23.1.2-linux.run
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.sudo /bin/rm -r /opt/mopac/

miroi@MIRO:~/work/software/mopac/. sudo ./mopac-22.1.1-linux.run

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.sudo ./mopac-23.1.2-linux.run

/opt/mopac  added to PATH

miroi@MIRO:~/work/software/mopac/.ldd /opt/mopac/bin/mopac
        linux-vdso.so.1 (0x00007ffe5b3e2000)
        libmopac.so.1 => /opt/mopac/bin/../lib/libmopac.so.1 (0x00007ff87818b000)
        libiomp5.so => /opt/mopac/bin/../lib/libiomp5.so (0x00007ff877c00000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ff87817f000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff878098000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007ff878093000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff8779d7000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff878071000)
        /lib64/ld-linux-x86-64.so.2 (0x00007ff87d8ea000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007ff87806c000)

install debichem packages
-------------------------
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/.sudo apt-get install debichem-semiempirical debichem-molecular-abinitio  debichem-molecular-dynamics  debichem-periodic-abinitio debichem-crystallography


