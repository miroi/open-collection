#
# https://fhi-aims-club.gitlab.io/tutorials/slab-calculations-and-surface-simulations-with-fhi-aims/P1-Creating_Structures/
#

from ase.build import diamond100

# Create the diamond 100 surface of Si directly using an utility function
sur = diamond100("Si", [1,1,6], a=5.43, vacuum = 20)

#sur.write("Si_100.in", scaled=True)
sur.write("Si_100.in")
