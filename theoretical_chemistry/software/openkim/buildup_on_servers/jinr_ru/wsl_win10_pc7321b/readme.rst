====================
OpenKIM on WSL-Win10
====================

install package
~~~~~~~~~~~~~~~
https://openkim.org/doc/usage/obtaining-models/#ubuntu_linux

sudo add-apt-repository ppa:openkim/latest
sudo apt-get update
sudo apt-get install libkim-api-dev openkim-models

problem
~~~~~~~
https://matsci.org/t/multiple-kim-installations-or-cannot-find-libkim-api-so/55164/3

sudo apt install pkgconf

pkg-config  libkim-api-dev openkim-models

pip3 install kimpy
Defaulting to user installation because normal site-packages is not writeable
Collecting kimpy
  Using cached kimpy-2.1.1.tar.gz (50 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy in /home/milias/.local/lib/python3.10/site-packages (from kimpy) (1.26.4)
Building wheels for collected packages: kimpy
  Building wheel for kimpy (pyproject.toml) ... done
  Created wheel for kimpy: filename=kimpy-2.1.1-cp310-cp310-linux_x86_64.whl size=23280193 sha256=4a119a172ed1b753b5cab304ba69e7689b3953b5a54a286b9a5ae6db43f2225c
  Stored in directory: /home/milias/.cache/pip/wheels/4a/a1/b6/42099de5d34d9eb5e7fe076fb5903221eee6b7bed67c596bcc
Successfully built kimpy
Installing collected packages: kimpy
Successfully installed kimpy-2.1.1


kim-api-collections
~~~~~~~~~~~~~~~~~~~
kim-api-collections-management  list > kim-api-collections-management_list.log


