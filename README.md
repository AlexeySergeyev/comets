# Serendipitous Comet Search in Archival Data

## Overview
This repository contains tools to search for serendipitous detections of comets of interest in all-sky survey data (ZTF, SDSS, Pan-STARRS, DECam, and LSST).


## Team
- Alexey Sergeyev (Observatoire de la Côte d'Azur)
- Jin Beniyama (Observatoire de la Côte d'Azur)


## Structure
```
data/                   # Raw data (FITS files, etc.)
docs/                   # Documentation
scripts/                # Executable scripts (.py, .sh, etc.)
temp/                   # Temporary or miscellaneous files
PS1_download.sh         # Script to download Pan-STARRS data
TODO.md                 # Task list
comets_visibility.ipynb # Notebook to retrieve filenames/links for comets
decam_download.ipynb    # Notebook to download DECam data
ztf_download.ipynb      # Notebook to download ZTF data
requirements.txt        # Python dependencies
```

## Setting up the Environment
We recommend using `venv` to ensure PS1 images are handled correctly.
This avoids known issues with `fits.open(fits_path)`.
See:
https://github.com/astropy/astropy/issues/15236

Create the virtual environment:
```
python3 -m venv venv
```
Activate it:
```
source venv/bin/activate
```
Install required packages:
```
pip install -r requirements.txt
```

## Dependencies
This repository is depending on `Python`, `NumPy`, `pandas`, `SciPy`, `Astropy`, `Astroquery`.


## LICENCE
This software is released under the MIT License.

