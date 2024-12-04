=======
Blender
=======


from https://docs.blender.org/api/current/info_quickstart.html

Scripting tab in Blender 4.3.0
==============================

PYTHON INTERACTIVE CONSOLE 3.11.9 (main, Oct 15 2024, 19:17:05) [MSC v.1929 64 bit (AMD64)]

Builtin Modules:       bpy, bpy.data, bpy.ops, bpy.props, bpy.types, bpy.context, bpy.utils, bgl, gpu, blf, mathutils
Convenience Imports:   from mathutils import *; from math import *
Convenience Variables: C = bpy.context, D = bpy.data

>>> list(bpy.data.objects)
[bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Light']]

>>> bpy.data.objects[0].name
'Camera'

>>> bpy.data.objects[1].name
'Cube'

>>> bpy.data.objects[2].name
'Light'

>>> bpy.data.objects[3].name
Traceback (most recent call last):
  File "<blender_console>", line 1, in <module>
IndexError: bpy_prop_collection[index]: index 3 out of range, size 3


simple print
~~~~~~~~~~~~
>>> print("Hello, blender ! Taken from   "+bpy.app.binary_path)
Hello, blender ! Taken from   C:\Program Files\Blender Foundation\Blender 4.3\blender.exe

