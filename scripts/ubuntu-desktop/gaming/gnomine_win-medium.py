#!/usr/bin/python3
import traceback, sys
try:
    import sys
    try:
        highscoresfile = open("/var/games/gnomine.Medium.scores")
    except IOError as e:
        # file does not exist
        sys.exit(1)
    bestscore = highscoresfile.readline()
    if not bestscore:
        #file empty
        sys.exit(1)
    #file not empty
    sys.exit(0)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
