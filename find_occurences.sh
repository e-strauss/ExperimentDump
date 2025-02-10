clear
current="$(pwd)"
echo $current
cd /Users/eliasstrauss/Desktop/TU/systemds-fork
cd scripts
echo "\nscripts:"
grep $1 -r . --colour
cd ../src/test/scripts
echo "\nsrc/test/scripts:"
grep $1 -r . --colour
cd $current
