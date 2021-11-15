#!/usr/bin/python3
import sys, os
homeDir = os.getenv('HOME')
sudoku_path = os.path.join(homeDir,'.config/gnome-sudoku/puzzles/')
try:
	#Load all finished games
	with open(sudoku_path+'finished', 'r') as finished:
		finished_games = list(finished)
	#Load all easy games
	with open(sudoku_path+'easy', 'r') as f:
		easy = f.read()
		for game in finished_games:
			#Lines in the files have a '/n' at the end.
			#Truncate before matching the finished list
			#with the list of easy games
			if game[:-1] in easy:
				#Easy game has been completed
				sys.exit(0)
		#No completed games found in easy
		sys.exit(1)
except IOError as e:
	#File does not exist or
	#List of game difficulty does not exist
	sys.exit(1)
