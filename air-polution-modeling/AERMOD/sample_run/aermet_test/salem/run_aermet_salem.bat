rem 
rem

echo "Spracovanie meteo/geograf dat pre Salem"
echo "...vyzaduje aermet.exe"

copy stage1.inp aermet.inp
aermet.exe
copy stage2.inp aermet.inp
aermet.exe
copy stage3.inp aermet.inp
aermet.exe

echo
echo "Hotovo, sfc a pfl subory su hotove !"

