#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download fits file with the link on CADC.

# Download only Pan-STARRS from C_2008FK75_visible.csv in fits_PS
>>> python3 scripts/download_fits_w_cadc_link.py C_2008FK75_visible.csv fits_PS  --inst Pan-STARRS1
"""
from argparse import ArgumentParser as ap
import pandas as pd
import os
import requests


if __name__ == "__main__":
    parser = ap(description="Download fits file with the link on CADC")
    parser.add_argument(
        "res", type=str,
        help="Preprocessed csv with the link to the data.")
    parser.add_argument(
        "outdir", type=str, 
        help="Output directory")
    parser.add_argument(
        "--inst", nargs="*", default=None,
        help="Instrument of interest")
    parser.add_argument(
        "--sep", type=str, default=",",
        help="Separator")
    args = parser.parse_args()
    
    df = pd.read_csv(args.res, sep=args.sep)

    # Make an output directory
    print()
    print(f"  Download data in {args.res}")
    print(f"  FITS files are saved in {args.outdir}")
    print()
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)
    
    col_inst = "Telescope/Instrument"
    # Output 
    insts = list(set(df[col_inst]))
    print(f"  Instuments ({col_inst}) in the input: {insts}")
    print()

    if args.inst is not None:
        print(f"  Only selected observations are saved.")
        # Original
        N0 = len(df)

        df_list = []
        for idx_inst, inst in enumerate(args.inst):
            df_inst = df[df[col_inst] == inst]
            N_inst = len(df_inst)
            df_list.append(df_inst)
            print(f"    {idx_inst+1}: {inst}, N={N_inst}")

        df = pd.concat(df_list)
        # After selection
        N1 = len(df)
        print(f"  {N1} out of {N0} are used.")
        print()

    
    col_link = "MetaData"
    url_ps_head, url_ps_tail = "http://ps1images.stsci.edu/", ".fits"
    for idx_fi, row in df.iterrows():
        inst = row[col_inst]

        # MetaData is empty for Pan-STARRS
        # Here somehow make a link to the fits file
        if inst == "Pan-STARRS1":
            # rings.v3.skycell.1796.025.wrp.r.55201_47598.fits -> ["rings.v3.skycell", "1796", "025", ...]
            image_name = row["Image"]
            parts = image_name.split(".")
            prefix = ".".join(parts[:3])   # rings.v3.skycell
            num1 = parts[3]                # 1796
            num2 = parts[4]                # 025

            link_fits = f"{url_ps_head}{prefix}/{num1}/{num2}/{image_name}.fits"

        else:
            link_fits = row[col_link]

        fi = link_fits.split("/")[-1]           
        out = os.path.join(outdir, fi)
        print(f"  {idx_fi+1}: Download {out} from {link_fits}.")

        if os.path.exists(out):
            print("  Already exist.")
            continue

        r = requests.get(link_fits, stream=True)
        r.raise_for_status()  
        
        # TODO: Check
        # SDSS data is like frame-g-001862-5-0115.fits.bz2 (~3 MB).
        # Is it better to download as frame-g-001862-5-0115.fits (~12 MB)?
        with open(out, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
