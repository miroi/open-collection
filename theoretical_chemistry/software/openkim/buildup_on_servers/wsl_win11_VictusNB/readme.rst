====================
OpenKIM on WSL-Win11
====================

install Ubuntu packages
~~~~~~~~~~~~~~~~~~~~~~~~
https://openkim.org/doc/usage/obtaining-models/#ubuntu_linux

sudo add-apt-repository ppa:openkim/latest
sudo apt-get update
sudo apt-get install libkim-api-dev openkim-models

https://matsci.org/t/multiple-kim-installations-or-cannot-find-libkim-api-so/55164/3

sudo apt install pkgconf

pkg-config  libkim-api-dev openkim-models

kimpy
~~~~~
https://pypi.org/project/kimpy/

pip3 install kimpy
.
.
Successfully built kimpy
Installing collected packages: kimpy
Successfully installed kimpy-2.1.1


kim-querry
~~~~~~~~~~
https://pypi.org/project/kim-query/

pip install kim-query
.
.
Installing collected packages: kim-query
Successfully installed kim-query-3.0.0

kim-api-collections
~~~~~~~~~~~~~~~~~~~
kim-api-collections-management  list > kim-api-collections-management_list.log


ls /lib/x86_64-linux-gnu/kim-api/
mod/  model-drivers/  portable-models/  simulator-models/

tests
-----
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/openkim/buildup_on_servers/wsl_win11_VictusNB/.python3 ase-kim-test.py
Potential energy: -0.37120682093323026 eV


