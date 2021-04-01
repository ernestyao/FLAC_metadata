#encoding:utf-8

from mutagen.flac import FLAC
import sys, os

def get_flac(flacpath):
    flaclist = []
    for dirs, dirnames, files in os.walk(flacpath):
        for file in files:
            if file.endswith('.flac'):
                flaclist.append(dirs+'/'+file)
    return flaclist

def set_info(file):
    #title, title_comp, title_mvt = ""
    flacfile = FLAC(file)
    title = flacfile["TITLE"]
    #print(title[0])
    # 根据“ - ”切割标题为title_comp, title_mvt
    if " - " in title[0]:
        title_comp, title_mvt = title[0].split(' - ', maxsplit=1)
    
        flacfile["Composition"] = title_comp
        flacfile["Movement"] = title_mvt
        #print(flacfile.tags)
        flacfile.save()


flac_dir = sys.argv[1]
flac_list = get_flac(flac_dir)
for file in flac_list:
    set_info(file)
