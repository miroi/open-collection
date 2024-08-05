ase-gpatom
==========

https://gitlab.com/gpatom/ase-gpatom/-/wikis/How-to-use-BEACON#first-example

Here's a simple example of finding the global minimum structure of Ag3Cu3 cluster with EMT potential


milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase-gpatom/first_example/.python3 beacon_example.py
Traceback (most recent call last):
  File "/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase-gpatom/first_example/beacon_example.py", line 22, in <module>
    go = BEACON(calc=calc,
  File "/home/milias/.local/lib/python3.10/site-packages/gpatom/beacon/beacon.py", line 238, in __init__
    self.set_initial_frames(use_forces=use_forces)
  File "/home/milias/.local/lib/python3.10/site-packages/gpatom/beacon/beacon.py", line 292, in set_initial_frames
    self.atomsio.write_xyz(self.atoms[i], strtype='init')
  File "/home/milias/.local/lib/python3.10/site-packages/gpatom/beacon/beacon.py", line 1308, in write_xyz
    write(filename, atoms, columns=columns,
  File "/home/milias/.local/lib/python3.10/site-packages/ase/io/formats.py", line 692, in write
    return _write(filename, fd, format, io, images,
  File "/home/milias/.local/lib/python3.10/site-packages/ase/parallel.py", line 271, in new_func
    return func(*args, **kwargs)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/io/formats.py", line 728, in _write
    return io.write(fd, images, **kwargs)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/io/formats.py", line 193, in _write_wrapper
    return function(*args, **kwargs)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/utils/__init__.py", line 577, in iofunc
    obj = func(fd, *args, **kwargs)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/io/extxyz.py", line 826, in write_xyz
    save_calc_results(atoms, calculator, calc_prefix="")
  File "/home/milias/.local/lib/python3.10/site-packages/ase/io/extxyz.py", line 989, in save_calc_results
    raise KeyError("key from calculator already exists in atoms.arrays")
KeyError: 'key from calculator already exists in atoms.arrays'
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase-gpatom/first_example/.

