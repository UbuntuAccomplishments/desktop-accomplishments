#!/usr/bin/python3
import subprocess, sys, os, traceback
try:
    homeDir = os.getenv("HOME")
    path = os.path.join(homeDir,'.config/user-dirs.dirs')
    result = open(path, "r")
    content = result.readline()
    documentDir = None
    while (content != "" ):
        content.replace( "\n", "" )
        content = result.readline()
        startStr = content[0:17]
        if startStr == 'XDG_DOCUMENTS_DIR':
            documentDir = content

    if documentDir is not None:
        documentDir = documentDir[21:]
        documentDir = documentDir[:-2]
    else:
        documentDir = 'Documents'

    fileCount = subprocess.check_output(['bash', '-c', 'ls {} -1 | wc -l'.format(os.path.join(homeDir, documentDir))]).strip().decode('utf-8').split(' ')
    fileCount =  fileCount[1:]
    if fileCount == 0:
        #user has no documents
        sys.exit(1)
    else:
        #user has documents
        sys.exit(0)

except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
