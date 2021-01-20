

for thefile in *.json.md ; do
   grep -v "<th>Scope</th>" $thefile > $thefile.$$.tmp
   mv $thefile.$$.tmp $thefile
done