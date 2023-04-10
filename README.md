# DoVi Check
### A script to check if your Dolby Vision file would run on an LG OLED

Before running the script, install its dependencies

```sh 
pip install pymediainfo colorama argparse
```
---
## **Usage:**
```shell
python3 dovi_check.py /path/to/file [--remux/-r]
```
If the video will not play on your LG TV, run the script again with the `--remux` flag and it will use ffmpeg to remux the .mkv file to .mp4 which *should* work. <br />

> **Warning** <br />
> Running this script on a mounted drive will force the whole file to be downloaded first

---