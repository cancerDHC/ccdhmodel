PARMS="--no-mergeimports"
for filename in model/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    echo Generating $filename
    gen-python $PARMS model/$BASE.yaml > ccdhmodel/$BASE.py
    rm -rf docs/$BASE
    gen-markdown $PARMS model/$BASE.yaml -d docs/$BASE -i
done
gen-jsonld-context $PARMS model/prefixes.yaml > includes/prefixes.context.jsonld