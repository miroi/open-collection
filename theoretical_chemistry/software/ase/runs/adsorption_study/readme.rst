===============================================
Surface adsorption study using the ASE database
===============================================

https://wiki.fysik.dtu.dk/ase/tutorials/db/db.html

python3 bulk.py 


milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/.ase db bulk.db -c +bm
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

ase db bulk.db Cu -j

milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/.file bulk.db
bulk.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 14, database pages 17, cookie 0xe, schema 4, UTF-8, version-valid-for 14

json
~~~~
milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/. ase db bulk.db --insert-into bulk.json
Added 0 key-value pairs (0 pairs updated)
Inserted 7 rows

Adsorptions
~~~~~~~~~~~
milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/.python3 ads.py

milias@pc7321b:/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/.ase db ads.db -n
126 rows


