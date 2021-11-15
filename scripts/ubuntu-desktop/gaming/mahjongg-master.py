#!/usr/bin/python3
import sys, os, traceback
try:
    runningTotal = 0
    #bridges
    filePath = '/var/games/mahjongg.bridges.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #cloud
    filePath = '/var/games/mahjongg.cloud.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #confounding
    filePath = '/var/games/mahjongg.confounding.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #difficult
    filePath = '/var/games/mahjongg.difficult.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #dragon
    filePath = '/var/games/mahjongg.dragon.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #easy
    filePath = '/var/games/mahjongg.easy.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #pyramid
    filePath = '/var/games/mahjongg.pyramid.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #tic-tac-toe
    filePath = '/var/games/mahjongg.tictactoe.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    #ziggurat
    filePath = '/var/games/mahjongg.ziggurat.scores'
    if not os.path.exists(filePath):
        sys.exit(1)
    fileSize = os.path.getsize(filePath)
    if fileSize > 0:
        runningTotal = runningTotal +1
    # 9 levels exist, therefore if running total is less than 9 then all
    # levels have not been completed
    if runningTotal < 9 :
        #user has not completed all mahjongg levels
        sys.exit(1)
    else:
        #user has completed all mahjongg levels
        sys.exit(0)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
