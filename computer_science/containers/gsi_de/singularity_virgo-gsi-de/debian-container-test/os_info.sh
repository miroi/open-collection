#!/usr/bin/env bash

cat /etc/os-release | head -2 ; uname -nr 

echo -e "pwd; ls; who:"
pwd
ls
who

echo -e "Number of processors:\c";cat /proc/cpuinfo | grep processor | wc -l

hostname -f

echo -e "which python"
which python

echo -e "which cmake"
which cmake

echo -e "which gcc"
which gcc

echo -e "which git"
which git


