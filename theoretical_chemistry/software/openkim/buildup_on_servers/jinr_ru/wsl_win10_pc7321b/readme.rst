====================
OpenKIM on WSL-Win10
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


kim-api-collections
~~~~~~~~~~~~~~~~~~~
kim-api-collections-management  list > kim-api-collections-management_list.log

kim-querry
~~~~~~~~~~
https://pypi.org/project/kim-query/

pip install kim-query
.
.
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests, kim-query
Successfully installed certifi-2024.7.4 charset-normalizer-3.3.2 idna-3.7 kim-query-3.0.0 requests-2.32.3 urllib3-2.2.2


