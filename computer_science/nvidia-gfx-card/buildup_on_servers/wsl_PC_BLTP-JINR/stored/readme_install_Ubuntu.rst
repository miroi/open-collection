======================
Install NVIDIA HPC SDK
=======================

https://developer.nvidia.com/hpc-sdk-downloads

Linux x86_64 Ubuntu(apt)
~~~~~~~~~~~~~~~~~~~~~~~~~

curl https://developer.download.nvidia.com/hpc-sdk/ubuntu/DEB-GPG-KEY-NVIDIA-HPC-SDK | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg
.
.
.



echo 'deb [signed-by=/usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg] https://developer.download.nvidia.com/hpc-sdk/ubuntu/amd64 /' | sudo tee /etc/apt/sources.list.d/nvhpc.list

sudo apt-get update -y 

sudo apt-get install -y nvhpc-25-7 
