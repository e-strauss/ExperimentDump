clear
current="$(pwd)"
echo $current
cd $SYSTEMDS_ROOT
cd scripts
echo "\nscripts:"
grep $1 -r . --colour
cd ../src/test/scripts
echo "\nsrc/test/scripts:"
grep $1 -r . --colour
cd $current
