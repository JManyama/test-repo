
cd ./src/slate-ui/build/

for thefile in *.json.md ; do
   grep -v "Scope Definition" $thefile > $thefile.$$.tmp
   mv $thefile.$$.tmp $thefile
done