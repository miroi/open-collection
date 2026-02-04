#
# https://wiki.fysik.dtu.dk/ase/ase/gui/basics.html#general-use
#

from ase.collections import g2
from ase.gui.gui import GUI

names = iter(g2.names)

def main(gui):
    try:
        name = next(names)
    except StopIteration:
        gui.window.win.quit()
    else:
        atoms = g2[name]
        gui.images.initialize([atoms])

gui = GUI()
gui.repeat_poll(main, 30)
gui.run()
