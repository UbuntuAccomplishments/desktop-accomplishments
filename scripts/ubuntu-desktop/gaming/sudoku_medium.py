#!/usr/bin/python3
import sys, os
homeDir = os.getenv('HOME')
sudoku_path = os.path.join(homeDir,'.config/gnome-sudoku/puzzles/')
def get_finished_levels():
	try:
		with open(sudoku_path+'finished', 'r') as finished:
			return (list(finished))
	except IOError as e:
		#file does not exist
		sys.exit(1)
finished_games = get_finished_levels()
try:
	with open(sudoku_path+'medium', 'r') as f:
		medium = f.read()
		for game in finished_games:
			#lines in the files have a '/n' at the end.
			#Truncate before checking
			if game[:-1] in medium:
				#easy game has been completed
				sys.exit(0)
		#No completed games found in easy
		sys.exit(1)
except IOError as e:
	#list of game difficulty does not exist
	sys.exit(1)
