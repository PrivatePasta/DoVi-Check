from pymediainfo import MediaInfo
import os
import json
import argparse
from colorama import Fore, Back, Style


def getFilePath() -> str:
    videoFile = input("Enter the path to the video file: ")

    # check if file exists
    if os.path.exists(videoFile):
        return videoFile

    print("File does not exist")


# Python is bad i dont wanna restructure
parsedMediaInfo = MediaInfo.parse(getFilePath())
parsedMediaInfoJSON = json.loads(parsedMediaInfo.to_json())
videoInfo = parsedMediaInfoJSON.get("tracks")[1]
infoArr = [
    "format",
    "format_profile",
    "hdr_format",
    "hdr_format_profile",
    "hdr_format_settings",
    "chroma_subsampling",
    "codec_id",
]


def getInfo(infoArr):
    for info in infoArr:
        print(info, ":", videoInfo.get(info))


def DoViCheck() -> bool:
    if videoInfo.get("hdr_format") == "Dolby Vision":
        return True
    else:
        return False


def DoViProfile5Check() -> bool:
    if videoInfo.get("hdr_format_profile") == "dvhe.05":
        return True


def willThisRun() -> bool:
    if DoViCheck() and DoViProfile5Check():
        return True
    else:
        return False

def remux_file(input_file: str, output_file: str):
    os.system(f"ffmpeg -i {input_file} -map 0:v:0 -c copy -map 0:a:2 -c copy {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Dolby Vision profile 5 compatibility checker')
    parser.add_argument('-r', '--remux', help='Remux the video file to mp4 format', action='store_true')
    args = parser.parse_args()

    if args.remux:
        video_file = getFilePath()
        if video_file.endswith('.mkv'):
            output_file = input("Enter the path for output file (with .mp4 extension): ")
            if not output_file.endswith('.mp4'):
                output_file += '.mp4'
            remux_file(video_file, output_file)
            print(f"\n{Fore.GREEN}Video remuxed successfully!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Invalid file format! File must be in .mkv format.{Style.RESET_ALL}")
        return

    print("\n")
    getInfo(infoArr)

    if willThisRun():
        print(
            "\n"
            + Back.LIGHTCYAN_EX
            + Fore.BLACK
            + " BASED "
            + Fore.LIGHTGREEN_EX
            + Back.BLACK
            + " This video is Dolby Vision profile 5 and is compatible with your LG TV"
            + Style.RESET_ALL
            + "\n"
        )
        if (
            parsedMediaInfoJSON.get("tracks")[0].get("file_extension") == "mkv"
        ) or parsedMediaInfoJSON.get("tracks")[0].get("other_format") == "Matroska":
            print(
                Back.LIGHTYELLOW_EX
                + Fore.BLACK
                + " Warning "
                + Fore.YELLOW
                + Back.BLACK
                + " This video is in mkv/Matroska container and will cause HDR fallback if available on your LG TV"
                + "\n"
                + Style.RESET_ALL
            )

    if DoViCheck():
        print(
            "\n"
            + Back.LIGHTWHITE_EX
            + Fore.BLACK
            + " ISSUE "
            + Fore.LIGHTRED_EX
            + Back.BLACK
            + " This video file is not Dolby Vision profile 5, and will not work on your LG TV"
            + Style.RESET_ALL
            + "\n"
        )

    else:
        print(
            "\n"
            + Back.LIGHTWHITE_EX
            + Fore.BLACK
            + " Skipped "
            + Fore.LIGHTRED_EX
            + Back.BLACK
            + " This video file is not Dolby Vision"
            + Style.RESET_ALL
            + "\n"
        )


if __name__ == "__main__":
    main()