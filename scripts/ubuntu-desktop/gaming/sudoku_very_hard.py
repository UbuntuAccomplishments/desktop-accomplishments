#!/usr/bin/python3
import sys, os
homeDir = os.getenv('HOME')
sudoku_path = os.path.join(homeDir,'.config/gnome-sudoku/puzzles/')
try:
	with open(sudoku_path+'finished', 'r') as finished:
		finished_games = list(finished)
	with open(sudoku_path+'very_hard', 'r') as f:
		very_hard = f.read()
		for game in finished_games:
			#lines in the files have a '/n' at the end.
			#Truncate before checking
			if game[:-1] in very_hard:
				#easy game has been completed
				sys.exit(0)
		#No completed games found in easy
		sys.exit(1)
except IOError as e:
	#file does not exist or
	#list of game difficulty does not exist
	sys.exit(1)
