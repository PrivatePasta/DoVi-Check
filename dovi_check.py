from pymediainfo import MediaInfo
import os
import json
from colorama import Fore, Back, Style


def getFilePath() -> str:
    videoFile = input("Enter the path to the video file: ")

    # check if file exists
    if os.path.exists(videoFile):
        return videoFile

    print('File does not exist')


# Python is bad i dont wanna restructure
parsedMediaInfo = MediaInfo.parse(getFilePath())
parsedMediaInfoJSON = json.loads(parsedMediaInfo.to_json())
videoInfo = parsedMediaInfoJSON.get('tracks')[1]
infoArr = ['format', 'format_profile', 'hdr_format', 'hdr_format_profile','hdr_format_settings', 'chroma_subsampling', 'codec_id']


def getInfo(infoArr):
    for info in infoArr:
        print(info, ':', videoInfo.get(info))


def DoViCheck() -> bool:
    if videoInfo.get('hdr_format') == 'Dolby Vision':
        return True
    else:
        return False


def DoViProfile5Check() -> bool:
    if videoInfo.get('hdr_format_profile') == 'dvhe.05':
        return True


def willThisRun() -> bool:
    if DoViCheck() and DoViProfile5Check():
        return True
    else:
        return False


def main():
    print('\n')
    getInfo(infoArr)

    if willThisRun():
        print('\n' + Back.LIGHTCYAN_EX + Fore.BLACK + ' BASED ' + Fore.LIGHTGREEN_EX + Back.BLACK + ' This video is DoVi profile 5 and is compatible with your TV' + Style.RESET_ALL + '\n')
        if (parsedMediaInfoJSON.get('tracks')[0].get('file_extension') == 'mkv') or parsedMediaInfoJSON.get('tracks')[0].get('other_format') == 'Matroska':
            print(Back.LIGHTYELLOW_EX + Fore.BLACK + ' Warning ' + Fore.YELLOW + Back.BLACK + ' This video is in mkv/Matroska container might cause issues in DoVi detection on your TV' + '\n' + Style.RESET_ALL)
    
    else if DoViCheck():
        print(
            '\n' + Back.LIGHTWHITE_EX + Fore.BLACK + ' ISSUE ' + Fore.LIGHTRED_EX + Back.BLACK + ' This video file is not DoVi profile 5, might not work on TV' + Style.RESET_ALL + '\n')

    else:
         print(
            '\n' + Back.LIGHTWHITE_EX + Fore.BLACK + ' Skipped ' + Fore.LIGHTRED_EX + Back.BLACK + ' This video file is not DoVi' + Style.RESET_ALL + '\n')


if __name__ == '__main__':
    main()
