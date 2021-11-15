#!/usr/bin/python3
import traceback, sys
try:
    try:
        highscoresfile = open("/var/games/gnomine.Small.scores")
    except IOError as e:
        # file does not exist
        sys.exit(1)
    bestscore = highscoresfile.readline()
    if not bestscore:
        #file empty
        sys.exit(1)
    #file not empty
    line = bestscore
    n = 0 #number of entries
    while line:
        n = n+1
        line = highscoresfile.readline()
    besttime = float(bestscore.split()[0])
    if besttime < 0.135:
        sys.exit(0)
    else:
        sys.exit(1)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
