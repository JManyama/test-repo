cd ./src/api-explorer/v3-0/

for g in *.json; do
  widdershins $g -o $g.md --user_templates "./templates/openapi3-copy"
done
