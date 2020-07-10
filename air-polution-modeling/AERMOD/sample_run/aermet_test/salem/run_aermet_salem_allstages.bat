rem 
rem
echo off

echo "Spracovanie meteo/geograf dat pre Salem"
echo "...vyzaduje aermet.exe"

echo "aermet.exe stage1.inp :"
aermet.exe stage1.inp

echo "aermet.exe stage2.inp :"
aermet.exe stage2.inp

echo "aermet.exe stage3.inp :"
aermet.exe stage3.inp

echo
echo "Hotovo, sfc a pfl subory pre AERMOD su hotove !"

