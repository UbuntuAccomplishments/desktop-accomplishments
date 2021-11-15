#!/usr/bin/python3
import os, sqlite3, sys
homeDir = os.getenv('HOME')
path = os.path.join(homeDir,'.local/share/shotwell/data/photo.db')
if os.path.exists(path):
	#Connect to Shotwell library db
	try:
		db = sqlite3.connect(path)
	except sqlite3.DatabaseError as e:
		#Corrupted database file
		print ("It seems that the Shotwell database has been corrupted.")
		sys.exit(1)

	cursor = db.cursor()
	cursor.execute('SELECT count(id) FROM PhotoTable')
	image_count = cursor.fetchone()
	cursor.execute('SELECT count(id) FROM VideoTable')
	video_count = cursor.fetchone()
	#Close the cursor and database
	cursor.close()
	db.close()
	if image_count[0] > 0 or video_count[0] > 0:
		#The user has images or videos in Shotwell
		sys.exit(0)
	else:
		#The user does not have images or videos in Shotwell
		sys.exit(1)
else:
	sys.exit(1)
