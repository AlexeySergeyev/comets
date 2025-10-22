#/bin.bash
#
# Download PS1 data in data/fits_PS_visible2
CSVDIR=data/visible2
OUTDIR=data
mkdir -p "$OUTDIR"

for f in "$CSVDIR"/*.csv; do
    # Extract csv
    fname=$(basename "$f")                   # C_2004D1_visible.csv
    comet=${fname%_visible.csv}               # C_2016R2
    comet_nounder=${comet//_/}                # C2016R2

    # Sub dir
    subdir="$OUTDIR/$comet_nounder/Pan-STARRS1"
    mkdir -p "$subdir"

    # Download
    python3 scripts/download_fits_w_cadc_link.py "$f" "$subdir" --inst Pan-STARRS1
    #echo $subdir
    
    # Remove if it is empty
    if [ -d "$subdir" ] && [ -z "$(ls -A "$subdir")" ]; then
        rmdir "$subdir"
        echo "Removed empty directory: $subdir"
    fi
    parentdir="$OUTDIR/$comet_nounder"
    if [ -d "$parentdir" ] && [ -z "$(ls -A "$parentdir")" ]; then
        rmdir "$parentdir"
        echo "Removed empty parent directory: $parentdir"
    fi
done
