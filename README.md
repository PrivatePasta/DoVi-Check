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
# Just and exmaple, refer: https://trac.ffmpeg.org/wiki/Map to map whatever video and audio needs to in your target mp4 file
# [-map] Used in situations when mp4 doesn't support some of the audio tracks from you mkv input
fmpeg -i <path/to/file>.mkv -map 0:v:0 -c copy -map 0:a:2 -c copy <target/file>.mp4
```
