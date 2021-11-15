#!/usr/bin/python3
import subprocess, sys, os
homeDir = os.getenv("HOME")
path = os.path.join(homeDir,'.config/user-dirs.dirs')
result = open(path, "r")
content = result.readline()
photosDir = None
while (content != "" ):
	content.replace( "\n", "" )
	content = result.readline()
	startStr = content[0:16]
	if startStr == 'XDG_PICTURES_DIR':
		photosDir = content
		print (photosDir)

# recursive function to go through sub-directories
def test_for_images(directory):
    dirList = os.listdir(directory)
    for fname in dirList:
        filepath = os.path.join(directory, fname)
        if os.path.isdir(filepath):
            test_for_images(filepath)
        else:
            filetype = subprocess.check_output(['file', '-b', filepath]).strip().decode('utf-8').split(' ')
            if len(filetype) > 1 and "image" in filetype[1]:
                # image file present
                sys.exit(0)

# removes extra characters around directory
if photosDir is not None:
    photosDir = photosDir[24:]
    photosDir = photosDir[:-2]
else:
    photosDir = "Pictures"

photos = os.path.join(homeDir, photosDir)
test_for_images(photos)
#user has no images
sys.exit(1)