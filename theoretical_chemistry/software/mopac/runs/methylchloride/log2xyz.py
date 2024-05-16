#!/usr/bin/env python
# coding: utf-8


import sys

def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1


fname_root = sys.argv[1]
fname_mop = fname_root + ".mop"
#fname_log = fname_root + ".log"
fname_log = "ch3cl_opt.aux"
fname_xyz = fname_root + ".xyz"
fname_dat = fname_root + ".dat"


fh_mop = open(fname_mop,"r")
all_lines_mop = fh_mop.readlines()

count_atoms = file_lengthy(fname_mop) - 3
atom_types = []
for i in range(count_atoms):
    atom_types.append(all_lines_mop[i + 3][:2])


fh_log = open(fname_log,"r")
all_lines_log = fh_log.readlines()
count_log = file_lengthy(fname_log)
num_step_opt = int(count_log / (count_atoms + 3))


atom_types = []
for i in range(count_atoms):
    atom_types.append(all_lines_mop[i + 3][:2])

atom_types = []
for i in range(count_atoms):
    atom_types.append(all_lines_mop[i + 3][:2])


fh_xyz = open(fname_xyz,"w")
fh_dat = open(fname_dat,"w")
for steps in range(num_step_opt):
    fh_xyz.write(str(count_atoms))
    fh_xyz.write("\n")
    energy_kcal_mol = all_lines_log[5  + steps * (count_atoms + 3)].partition("+")[2].partition("\n")[0]

    print (energy_kcal_mol)

    energy_kcal_mol = float(energy_kcal_mol.replace("D", "E"))

    energy_kJ = round(energy_kcal_mol * 4.1868, 3)

    fh_dat.write(str(steps) + "\t" + str(energy_kcal_mol) + "\n")
    fh_xyz.write("Profile " + str(steps + 1) + " HEAT OF FORMATION =    " + str(energy_kcal_mol) + " KCAL =    " + str(energy_kJ) + " KJ")
    fh_xyz.write("\n")
    for x in range(count_atoms):
        atom_coord = all_lines_log[8 + steps * (count_atoms + 3) + x]
        fh_xyz.write(atom_types[x] + atom_coord)

fh_xyz.close()
fh_dat.close()
