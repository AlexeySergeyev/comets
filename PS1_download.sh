#/bin.bash
#
# Download PS1 data in data/fits_PS_visible2
CSVDIR=data/visible2
OUTDIR=data/fits_PS_visible2
mkdir -p "$OUTDIR"

for f in $CSVDIR/*.csv; 
do
    #echo "$f"
    python3 scripts/download_fits_w_cadc_link.py $f $OUTDIR --inst Pan-STARRS1
done

