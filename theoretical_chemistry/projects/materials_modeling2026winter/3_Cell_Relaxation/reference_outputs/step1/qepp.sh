#!/bin/bash
#post processing script for Quantum ESPRESSO v3.9


# default values if not set in input
calc=0
calculation="scf"
nstep=50


#check and backup files
for file in "final_structure.vasp" "final_relaxed_structure.vasp"; do
    [ -e "$file" ] && mv -f -- "$file" "${file}_asebackup"
done
for file in "final_structure.pwi" "final_relaxed_structure.pwi"; do
    [ -e "$file" ] && mv -f -- "$file" "${file}_asebackup"
done
for file in *.pwi; do
    [ -e "$file" ] || continue
    cp "$file" "${file%.pwi}.in"
	echo "Found ASE-QE input."
done
for file in *.pwo; do
    [ -e "$file" ] || continue
    cp "$file" "${file%.pwo}.out"
	echo "Found ASE-QE output."
done
if [ ! -f *.in ]; then
    echo "Input file does not exist."
	echo "Exiting..."
	exit
fi
if [ ! -f *.out ]; then
	echo "Output file not found. Only Input file will be processed."
	calc=4
	calculation="input"
fi
if [ -f *.qe ]; then
	rm *.qe
	echo "Clearing old *.qe files."
fi
if [ -f *.vasp ]; then
	rm *.vasp
	echo "Clearing old *.vasp files."
fi
if [ -f *.ase ]; then
	rm *.ase
	echo "Clearing old *.ase files."
fi


#check symmetry
grep -i ibrav *.in > ibrav1
sed -r 's/.*/\L&/g' ibrav1 > ibrav2
sed -r 's/\s+//g' ibrav2 > ibrav3
. ibrav3
rm ibrav1 ibrav2 ibrav3
if [ $ibrav -gt 0 ]; then
		echo "$ibrav ibrav > 0 not supported."
		exit
fi


#read input parameters
#nat
grep -i nat *.in > nat1
sed -r 's/.*/\L&/g' nat1 > nat2
sed -r 's/\s+//g' nat2 > nat3
. nat3
rm nat1 nat2 nat3

#ntyp
grep -i ntyp *.in > ntyp1
sed -r 's/.*/\L&/g' ntyp1 > ntyp2
sed -r 's/\s+//g' ntyp2 > ntyp3
. ntyp3
rm ntyp1 ntyp2 ntyp3

#calculation type
if [ $calc == 0 ]; then
	grep calculation *.in > calculation1
	sed -r 's/.*/\L&/g' calculation1 > calculation2
	sed -r 's/\s+//g' calculation2 > calculation3
	. calculation3
	rm calculation1 calculation2 calculation3
fi

#nstep for geometry optimization runs. if not found in *.in, default is 50 
if [ $calculation == "vc-relax" ] || [ $calculation == "relax" ]; then
	grep -i nstep *.in > nstep1
	sed -r 's/.*/\L&/g' nstep1 > nstep2
	sed -r 's/\s+//g' nstep2 > nstep3
	. nstep3
	rm nstep1 nstep2 nstep3
fi


#atomic species and their counts
grep -A $nat "ATOMIC_POSITIONS" *.in|tail -$nat > tempdata
grep -A $ntyp "ATOMIC_SPECIES" *.in|tail -$ntyp > species1
awk '{print $1}' species1 > species2
readarray species < species2
	for item in "${species[@]}"
	do grep -w $item tempdata | wc -l >> count1;
	done
readarray count < count1
rm species1 species2 count1 tempdata
count=("${count[@]%$'\n'}")
species=("${species[@]%$'\n'}")
for ((i=0; i<$ntyp; i=i+1))
	do echo -n "${species[i]}${count[i]}" >> atoms
done
atoms=$(head -1 atoms)
rm atoms


#check convergence status and print some useful info
if [ $calculation == "vc-relax" ]; then
	echo
	calc=1
	calculation=${atoms}_$calculation
	echo "Variable cell relaxation. Run a seperate SCF calculation to get total energy."
	if (grep -q 'final coordinates' *.out); then
		echo "Calculation converged."
		convergence_info=$(grep "converged in" *.out)
		echo $convergence_info
		grep "Total force" *.out | tail -1 > final_force1
		awk '{print "Final_force="$4}' final_force1 >> final_force2
		rm final_force1
		. final_force2
		echo "Final total force is $Final_force Ry/au."
		rm final_force2
	else
		convergence_info=$( grep -c "ATOMIC_POSITIONS" *.out)
		if [ $convergence_info == 0 ]; then
			calc=4
			calculation=NOT_STARTED_$calculation
			echo "0 SCF cycles were completed. No structural data in the output file."
			echo "Only Input file will be processed."
		else
			calc=5
			calculation=NOT_CONVERGED_$calculation
			echo "$convergence_info scf cycles out of $nstep were run."
			echo "Calculation did not converge."
			grep "Total force" *.out | tail -1 > last_force1
			awk '{print "last_force="$4}' last_force1 >> last_force2
			rm last_force1
			. last_force2
			echo "Last total force is $last_force Ry/au."
			rm last_force2
			echo "Continue structural optimization from the extracted coordinates till convergence is reached."
		fi
	fi
	
elif [ $calculation == "relax" ]; then
	echo
	calc=2
	calculation=${atoms}_$calculation
	echo "Only atomic relaxation. Run a seperate SCF calculation to obtain accurate total energy."
	if (grep -q 'final coordinates' *.out); then
		echo "Calculation converged."
		convergence_info=$(grep "converged in" *.out)
		echo $convergence_info
		grep "Total force" *.out | tail -1 > final_force1
		awk '{print "Final_force="$4}' final_force1 >> final_force2
		rm final_force1
		. final_force2
		echo "Final total force is $Final_force Ry/au."
		rm final_force2
	else
		convergence_info=$( grep -c "ATOMIC_POSITIONS" *.out)
		if [ $convergence_info == 0 ]; then
			calc=4
			calculation=NOT_STARTED_$calculation
			echo "0 SCF cycles were completed. No structural data in the output file."
			echo "Only Input file will be processed."
		else
			calc=6
			calculation=NOT_CONVERGED_$calculation
			echo "$convergence_info scf cycles out of $nstep were run."
			echo "Calculation did not converge."
			grep "Total force" *.out | tail -1 > last_force1
			awk '{print "last_force="$4}' last_force1 >> last_force2
			rm last_force1
			. last_force2
			echo "Last total force is $last_force Ry/au."
			rm last_force2
			echo "Continue structural optimization from the extracted coordinates till convergence is reached."
		fi
	fi
	
elif [ $calculation == "scf" ]; then
		echo
		calc=3
		calculation=${atoms}_$calculation
		if grep -q "convergence has been" *.out; then
			echo "SCF calculation."
			convergence_info=$(grep "convergence has been" *.out)
			echo $convergence_info
			grep ! *.out > energy1
			awk '{print "Energy="$5}' energy1 > energy2
			rm energy1
			. energy2
			echo "Total Energy is $Energy Ry."
			rm energy2
		else
			echo "SCF calculation did not converge."
			calculation=NOT_CONVERGED_$calculation
		fi

elif [ $calculation == "input" ]; then
		calculation=${atoms}_$calculation
fi


echo


#extract coordinates in *.qe file
# index: 1)vc-relax 2) relax 3) SCF 4) input 5) not-converged vc-relax 6) not-converged relax
if [ $calc == 1 ]; then
	sed -n '/Begin final coordinates/,/End final coordinates/p' *.out > temp1
	grep -A 3 "CELL_PARAMETERS" temp1 > $calculation.qe
	grep -A $nat "ATOMIC_POSITIONS" temp1 >> $calculation.qe
	echo "Reading both cell parameters and atomic positions from OUTPUT."
	rm temp1
elif [ $calc == 2 ]; then
	grep -A 3 "CELL_PARAMETERS" *.in > $calculation.qe
	sed -n '/Begin final coordinates/,/End final coordinates/p' *.out > temp2
	grep -A $nat "ATOMIC_POSITIONS" temp2 >> $calculation.qe
	echo "Reading cell parameters from INPUT and atomic positions from OUTPUT."
	rm temp2
elif [ $calc == 3 ]; then
	grep -A 3 "CELL_PARAMETERS" *.in > $calculation.qe
	grep -A $nat "ATOMIC_POSITIONS" *.in >> $calculation.qe
	echo "Reading both cell parameters and atomic positions from INPUT."
elif [ $calc == 4 ]; then
	grep -A 3 "CELL_PARAMETERS" *.in > $calculation.qe
	grep -A $nat "ATOMIC_POSITIONS" *.in >> $calculation.qe
	echo "Reading both cell Parameters and atomic positions from INPUT."
elif [ $calc == 5 ]; then
	grep -A 3 "CELL_PARAMETERS" *.out|tail -4 > $calculation.qe
	nat_1=$((nat + 1))
	grep -A $nat "ATOMIC_POSITIONS" *.out|tail -$nat_1 >> $calculation.qe
	echo "Reading last values of both cell parameters and atomic positions from OUTPUT."
elif [ $calc == 6 ]; then
	grep -A 3 "CELL_PARAMETERS" *.in > $calculation.qe
	nat_1=$((nat + 1))
	grep -A $nat "ATOMIC_POSITIONS" *.out|tail -$nat_1 >> $calculation.qe
	echo "Reading cell parameters from INPUT and last values of atomic positions from OUTPUT."
fi


#print some useful info
echo "Cell parameters and atomic positions extracted in $calculation.qe file."
echo
echo "In total, there are $nat atom(s)"
echo "There are $ntyp type(s) of atom(s)"
for ((i=0; i<$ntyp; i=i+1))
do echo "There are ${count[i]} ${species[i]} atom(s)"
done


echo


#check cell unit
cunit=0
cbohr=0
grep "CELL_PARAMETERS" $calculation.qe > pcell
grep -q -i 'angstrom' pcell
statuspcell=$?
if [ $statuspcell == 0 ]; then 
		echo "Cell parameters are in Angstorm"
		cunit=Angstorm
fi
grep -q -i 'bohr' pcell
statuspcell=$?
if [ $statuspcell == 0 ]; then 
		cunit=Bohr
		cbohr=1
		echo "Cell parameters are in Bohr"
		grep -A 3 "CELL_PARAMETERS" $calculation.qe > cbohrtemp
		tail -n +2 "cbohrtemp" > cbohrtemp2
		awk '{for (i=1; i<=3; i++) $i=$i*0.529177249; print}' cbohrtemp2 >> cbohrtemp3
		echo "CELL_PARAMETERS Angstorm" > $calculation.qe_cbohr
		cat cbohrtemp3 >> $calculation.qe_cbohr
		grep -A $nat "ATOMIC_POSITIONS" $calculation.qe >> $calculation.qe_cbohr
		echo "Converting lattice parameters from Bohr to Angstorm for VASP"
		rm cbohrtemp cbohrtemp2 cbohrtemp3
fi
if [ $cunit == 0 ]; then 
		echo "Cell parameters must be in Angstorm or Bohr only"
		exit
fi
rm pcell


#check positions unit
aunit=0
abohr=0
grep "ATOMIC_POSITIONS" $calculation.qe > patom
grep -q -i 'angstrom' patom
statuspatom=$?
if [ $statuspatom == 0 ]; then 
		echo "Atomic positions are in Angstorm"
		aunit=Cartesian
fi
grep -q -i 'crystal' patom
statuspatom=$?
if [ $statuspatom == 0 ]; then 
		echo "Atomic positions are in fractional coordinates"
		aunit=Direct
fi
grep -q -i 'bohr' patom
statuspatom=$?
if [ $statuspatom == 0 ]; then 
		aunit=Cartesian
		abohr=1
		echo "Atomic positions are in Bohr"
		grep -A $nat "ATOMIC_POSITIONS" $calculation.qe > abohrtemp
		tail -n +2 "abohrtemp" > abohrtemp2
		awk '{for (i=2; i<=4; i++) $i=$i*0.529177249; print}' abohrtemp2 >> abohrtemp3
		grep -A 3 "CELL_PARAMETERS" $calculation.qe > $calculation.qe_abohr
		echo "ATOMIC_POSITIONS Angstorm" >> $calculation.qe_abohr
		echo "Converting atomic positions from Bohr to Angstorm for VASP"
		cat abohrtemp3 >> $calculation.qe_abohr
		rm abohrtemp abohrtemp2 abohrtemp3
	fi
if [ $aunit == 0 ]; then 
		echo "Atomic positions must be in Angstorm, Bohr or fractional coordinate only"
		exit
fi
rm patom


#convert to Vesta
echo
echo "Exporting structure to Vesta readable format: $calculation.vasp"
for ((i=0; i<$ntyp; i=i+1))
	do echo -n "${species[i]}${count[i]}" >> $calculation.vasp
done
echo " (coordinates from $calculation)"  >> $calculation.vasp
echo "1.0" >> $calculation.vasp
if [ $cbohr == 0 ]; then 
	grep -A 3 "CELL_PARAMETERS" $calculation.qe | tail -3 >> $calculation.vasp
else 
	grep -A 3 "CELL_PARAMETERS" $calculation.qe_cbohr |  tail -3 >> $calculation.vasp
	rm $calculation.qe_cbohr
fi
for ((i=0; i<$ntyp; i=i+1))
	do echo -n "${species[i]}  " >> $calculation.vasp
	done
echo >> $calculation.vasp
for ((i=0; i<$ntyp; i=i+1))
	do echo -n "${count[i]}  " >> $calculation.vasp
done
echo >> $calculation.vasp
echo "$aunit" >> $calculation.vasp
if [ $abohr == 0 ]; then 
	grep -A $nat "ATOMIC_POSITIONS" $calculation.qe |  tail -$nat >> temp.vasp
else 
	grep -A $nat "ATOMIC_POSITIONS" $calculation.qe_abohr |  tail -$nat >> temp.vasp
	rm $calculation.qe_abohr
fi
awk '{print "\t"$2"\t"$3"\t"$4}' temp.vasp >> $calculation.vasp
cp temp.vasp temp.ase
rm temp.vasp


#convert to ASE
if [ "$cunit" = "Angstorm" ] && [ "$aunit" = "Cartesian" ]; then
	echo "Exporting ASE format: $calculation.ase"
	sed -i 's/[[:space:]]*$//' temp.ase
	echo -e -n "\tsymbols=" >> $calculation.ase
	for ((i=0; i<$ntyp; i=i+1))
		do echo -n "['${species[i]}']*${count[i]}" >> $calculation.ase
		if [ $i -lt $(($ntyp - 1)) ]; then
		echo -n " + " >> $calculation.ase
		fi
		if [ $i == $(($ntyp - 1)) ]; then
		echo -n "," >> $calculation.ase
		fi
	done
	echo -e "\n\tpositions=[ # positions in Angstrom" >> $calculation.ase
	awk '{print "\t""\t""["$2", "$3", "$4"],"}' temp.ase >> $calculation.ase
	echo -e "\t],"  >> $calculation.ase
	echo -e "\tcell=[ # positions in Angstrom" >> $calculation.ase
	grep -A 3 "CELL_PARAMETERS" $calculation.qe | tail -3 >> temp2.ase
	sed -i 's/[[:space:]]*$//' temp2.ase
	awk '{print "\t""\t""["$1", "$2", "$3"],"}' temp2.ase >> $calculation.ase
	echo -e "\t],"  >> $calculation.ase
else 
	echo "Cell parameters or atomic positions are not in Angstorm."
	echo "ASE format not exported."
fi
rm temp.ase
if [ -f temp2.ase ]; then
	rm temp2.ase
fi


