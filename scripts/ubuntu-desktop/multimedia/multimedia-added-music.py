#!/usr/bin/python3
import subprocess, sys, os
homeDir = os.getenv("HOME")
path = os.path.join(homeDir,'.config/user-dirs.dirs')
result = open(path, "r")
content = result.readline()
musicDir = None
while (content != "" ):
	content.replace( "\n", "" )
	content = result.readline()
	startStr = content[0:13]
	if startStr == 'XDG_MUSIC_DIR':
		musicDir = content

# recursive function to go through sub-directories
def test_for_music(directory):
    dirList = os.listdir(directory)
    for fname in dirList:
        filepath = os.path.join(directory, fname)
        if os.path.isdir(filepath):
            test_for_music(filepath)
        else:
            filetype = subprocess.check_output(['file', '-b', filepath]).strip().decode('utf-8').split(' ')
            if len(filetype) > 1 and "audio" in filetype[1]:
                # audio file present
                sys.exit(0)

# removes extra characters around directory
if musicDir is not None:
    musicDir = musicDir[21:]
    musicDir = musicDir[:-2]
else:
    musicDir = "Music"

music = os.path.join(homeDir, musicDir)
test_for_music(music)
#user has no music
sys.exit(1)
