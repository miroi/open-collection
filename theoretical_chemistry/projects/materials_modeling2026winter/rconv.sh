#!/bin/bash

echo "Energy and force convergence for vc-relax runs"
echo "------------------------------------"
echo "Cut off  Total Energy  Total Force"
echo " (Ry)       (Ry)        (Ry/au)"
echo "------------------------------------"
awk '/kinetic-energy/{ecut=$4}
     /!.*total/{etot=$5}
     /Total force/{print ecut, etot, $4}' *out
echo "------------------------------------"
