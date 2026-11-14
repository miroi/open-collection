import io, os, tempfile, contextlib
import numpy as np
from ase import Atoms
from jarvis.core.atoms import ase_to_atoms
from alignn.pretrained import get_prediction

CUTOFF, BOX = 5.0, 60.0
TARGETS = ["gap", "ZPVE", "alpha", "U0"]
CONV = {"gap": (6.8587, 1.2843), "ZPVE": (4.0568, 0.9017), "alpha": (75.19, 8.19)}  # approximate
ANGLE = 103.7

def water(r, angle=ANGLE):
    t = np.radians(angle / 2)
    a = Atoms("OHH", positions=[[0, 0, 0], [r * np.sin(t), r * np.cos(t), 0],
                                [-r * np.sin(t), r * np.cos(t), 0]])
    a.set_cell([BOX] * 3); a.pbc = True; a.center()
    return a

workdir = tempfile.TemporaryDirectory(); os.chdir(workdir.name)
print(f"{'r_OH':>6s}" + "".join(f"{t:>10s}" for t in TARGETS))
for r in np.arange(0.950, 0.9801, 0.005):
    ja = ase_to_atoms(water(r))
    row = []
    for t in TARGETS:
        with contextlib.redirect_stdout(io.StringIO()):
            z = float(np.ravel(get_prediction(model_name=f"qm9_{t}_alignn", atoms=ja, cutoff=CUTOFF))[0])
        row.append(z * CONV[t][1] + CONV[t][0] if t in CONV else z)
    print(f"{r:6.3f}" + "".join(f"{v:10.3f}" for v in row))
os.chdir("/"); workdir.cleanup()
