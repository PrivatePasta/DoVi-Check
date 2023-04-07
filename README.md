# DoVi Check
### A script to check if your Dolby Vision file would run on an LG OLED

Before running the script, install its dependencies

```sh 
pip install pymediainfo colorama
```
> **Warning** <br />
> Running this script on a mounted drive will force the whole file to be downloaded first

---

> **Note** <br /> 
> If the only reason you're having issues is because it's in an **mkv** container use this to remux it in **mp4**

```sh
fmpeg -i <path/to/file>.mkv -map 0:v:0 -c copy -map 0:a:2 -c copy <target/file>.mp4
```
