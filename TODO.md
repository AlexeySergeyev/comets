# Comet download

Initial




- [x] Fetch CADEC dataset (`comet_cadec.csv`)
- [x] Fetch Miriade dataset (`comet_miriade.csv`)
- [x] Fetch JPL Horizons dataset (`comet_jplhorizons.csv`)

TODO:


- [x] For each of telescopes/instruments filters, set magnitude range accordingly.

- [x] Select observations with a magnitude brighter than a given magnitude limits based on 
the survey filter limit table [Survey filter limits](data/Survey-Filters-LimitingMagtypicalexposure-TypicalExposureTimes-Reference.csv)

Write a function to download Images from Instruments/Telescope for given dates.

- [ ] Write function to download images from PS1 for given dates (Jin)
- [ ] Write function to download images from ZTF for given dates (Alexey)
- [ ] Write function to download images from DECam for given dates (Alexey, Jin)
- [ ] Write function to download images from SDSS for given dates (Alexey)

``` python
def download_images_ps1(href):
    pass

def cutoff_comet_ps1(file_path, ra, dec, fov=10 * u.arcmin,
                     output_path="data/ps1/comets/", is_plot=False):
    pass

... similar for ZTF, DECam, SDSS
```