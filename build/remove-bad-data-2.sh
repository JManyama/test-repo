
cd ./src/Slate-API-Explorer-Reference/slate/source/includes/

for thefile in *.json.md ; do
   grep -v "<th>Scope Definition</th>" $thefile > $thefile.$$.tmp
   mv $thefile.$$.tmp $thefile
done