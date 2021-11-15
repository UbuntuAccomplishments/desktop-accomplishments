#!/usr/bin/python3
import sys, os
homeDir = os.getenv("HOME")
path = os.path.join(homeDir,'.local/share/rhythmbox/rhythmdb.xml')
if os.path.exists(path):
	#user has used Rhythmbox now we need to test for the existence of music
        # test for the existence of <entry type="song"> in the rhythmdb.xml
        file = open(path)
        # convert file to string
        data = file.read()
        # we do not need to keep the file open
        file.close()
        # test for the existence of a song in the file
        if "song" in data:
                #user has music in Rhythmbox
                sys.exit(0)
                # print "user has music"
        else:
                #user does not have music in Rhythmbox
                sys.exit(1)
                # print "user does not have music"
else:
        # user has not used Rhythmbox
	sys.exit(1)
