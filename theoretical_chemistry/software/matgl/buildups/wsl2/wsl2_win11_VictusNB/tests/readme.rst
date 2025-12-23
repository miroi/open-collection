Simple test
===========

https://github.com/materialyzeai/matgl#code

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/tests/.python formation_energy_CsCl.py
/home/miroi/work/software/myenv/lib/python3.12/site-packages/matgl/utils/io.py:244: UserWarning: Model MEGNet is a DGL model, but the backend is PYG. Setting the backend to DGL.
  return cls_.load(fpaths, **kwargs)
Traceback (most recent call last):
  File "/home/miroi/work/software/myenv/lib/python3.12/site-packages/matgl/utils/io.py", line 244, in load_model
    return cls_.load(fpaths, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/work/software/myenv/lib/python3.12/site-packages/matgl/utils/io.py", line 157, in load
    mod = __import__(modname, globals(), locals(), [classname], 0)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/work/software/myenv/lib/python3.12/site-packages/matgl/models/_megnet.py", line 16, in <module>
    from dgl.nn import Set2Set
ModuleNotFoundError: No module named 'dgl'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/miroi/work/projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win11_VictusNB/tests/formation_energy_CsCl.py", line 6, in <module>
    model = matgl.load_model("MEGNet-MP-2018.6.1-Eform")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/work/software/myenv/lib/python3.12/site-packages/matgl/utils/io.py", line 246, in load_model
    raise ValueError(
ValueError: Bad serialized model or bad model name. There are several possible causes. If you are using a DGL model, you need to set the backend to DGL using `matgl.set_backend('DGL')`. If you have an outdated cached model, please 'clear your cache by running `python -c 'import matgl; matgl.clear_cache()'`

