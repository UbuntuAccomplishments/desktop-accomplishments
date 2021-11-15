#!/usr/bin/python3
import sys, os, traceback
try:
    filePath = '/var/games/mahjongg.cloud.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        #user has completed mahjongg cloud level
        sys.exit(0)
    else:
        #user has not completed mahjongg cloud level
        sys.exit(1)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
