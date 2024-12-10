===============================================
Surface adsorption study using the ASE database
===============================================

https://wiki.fysik.dtu.dk/ase/tutorials/db/db.html

In this tutorial we will adsorb C, N and O on 7 different FCC(111) surfaces with 1, 2 and 3 layers and we will use database files to store the results.

equilibrium bulk FCC
~~~~~~~~~~~~~~~~~~~~
First, we calculate the equilibrium bulk FCC lattice constants for the seven elements where the EMT potential works well:

python3 bulk.py
Al fcc crystal energy: -0.004882682308843922
Ni fcc crystal energy: -0.013306890189579867
Cu fcc crystal energy: -0.007036492048374754
Pd fcc crystal energy: -0.00026992497101518964
Ag fcc crystal energy: -0.00036686253917483924
Pt fcc crystal energy: -0.00014952704168358366
Au fcc crystal energy: -0.00013514121662172585


print the database content
~~~~~~~~~~~~~~~~~~~~~~~~~~
show also the bulk-modulus column :

ase db bulk.db -c +bm
id|age|user  |formula|calculator|energy|natoms| fmax|pbc|volume|charge|   mass|   bm
 1|52s|milias|Al     |emt       |-0.005|     1|0.000|TTT|15.932| 0.000| 26.982|0.249
 2|51s|milias|Ni     |emt       |-0.013|     1|0.000|TTT|10.601| 0.000| 58.693|1.105
 3|51s|milias|Cu     |emt       |-0.007|     1|0.000|TTT|11.565| 0.000| 63.546|0.839
 4|51s|milias|Pd     |emt       |-0.000|     1|0.000|TTT|14.588| 0.000|106.420|1.118
 5|51s|milias|Ag     |emt       |-0.000|     1|0.000|TTT|16.775| 0.000|107.868|0.625
 6|51s|milias|Pt     |emt       |-0.000|     1|0.000|TTT|15.080| 0.000|195.084|1.736
 7|51s|milias|Au     |emt       |-0.000|     1|0.000|TTT|16.684| 0.000|196.967|1.085
Rows: 7
Keys: bm

file bulk.db
bulk.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 14, database pages 17, cookie 0xe, schema 4, UTF-8, version-valid-for 14

ase db bulk.db Cu -j

file bulk.db
bulk.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 14, database pages 17, cookie 0xe, schema 4, UTF-8, version-valid-for 14

json
~~~~
ase db bulk.db --insert-into bulk.json
Added 0 key-value pairs (0 pairs updated)
Inserted 7 rows

Adsorptions
~~~~~~~~~~~
python3 ads.py

ase db ads.db -n
63 rows

Reference energies of surfaces and atoms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let’s also calculate the energy of the clean surfaces and the isolated adsorbates

python3 refs.py

ase db ads.db -n
87 rows


manipulating db
~~~~~~~~~~~~~~~
ase db ads.db ads=clean --insert-into refs.db
Added 0 key-value pairs (0 pairs updated)
Inserted 21 rows

ase db ads.db ads=clean --delete --yes
Deleted 21 rows

ase db ads.db pbc=FFF --insert-into refs.db
Added 0 key-value pairs (0 pairs updated)
Inserted 3 rows

ase db ads.db pbc=FFF --delete --yes
Deleted 3 rows

ase db ads.db -n
63 rows

ase db refs.db -n
24 rows

Analysis
~~~~~~~~
Now we have what we need to calculate the adsorption energies and heights

python3 ea.py

ase db ads.db Pt,layers=3 -c formula,ea,height
formula|    ea|height
Pt3C   |-3.715| 1.503
Pt3N   |-5.419| 1.535
Pt3O   |-4.724| 1.706
Rows: 3
Keys: ads, ea, height, layers, surf

ase db ads.db Au,layers=3 -c formula,ea,height
formula|    ea|height
Au3C   |-3.547| 1.485
Au3N   |-5.281| 1.499
Au3O   |-4.603| 1.696
Rows: 3
Keys: ads, ea, height, layers, surf

ase db ads.db Ag,layers=3 -c formula,ea,height
formula|    ea|height
Ag3C   |-3.560| 1.377
Ag3N   |-5.336| 1.375
Ag3O   |-4.592| 1.599
Rows: 3
Keys: ads, ea, height, layers, surf

