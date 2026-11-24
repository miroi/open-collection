===============================
AceFF Model with ASE under WSL2
===============================

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/aimnet2-ase/wsl2/.pip install torchmd-net -i https://mirrors.aliyun.com/pypi/simple/
.
.
Successfully built torchmd-net
Installing collected packages: xxhash, psutil, torch_geometric, torchmd-net
Successfully installed psutil-7.2.2 torch_geometric-2.8.1 torchmd-net-3.1.0 xxhash-4.1.0

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/aceff-ase/wsl2/.curl -L -o aceff_v2.0.ckpt https://huggingface.co/Acellera/AceFF-2.0/resolve/main/aceff_v2.0.ckpt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1031  100  1031    0     0   3748      0 --:--:-- --:--:-- --:--:--  3762
100 11.4M  100 11.4M    0     0  5720k      0  0:00:02  0:00:02 --:--:-- 7036k

pip install huggingface_hub
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting huggingface_hub
.
.
Installing collected packages: truststore, hf-xet, anyio, httpcore2, httpx2, huggingface_hub
Successfully installed anyio-4.16.0 hf-xet-1.8.0 httpcore2-2.16.0 httpx2-2.16.0 huggingface_hub-2.4.0 truststore-0.10.5


AceFF-2.0 is trained for small drug-like molecules (≤30 atoms, elements H/B/C/N/O/F/Si/P/S/Cl/Br/I), charges −2…+2. Do not apply it to proteins, water, or periodic solids.


deepseek
--------
https://chat.deepseek.com/share/q3hzadmx2968gbeevu



