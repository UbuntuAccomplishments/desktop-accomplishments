#!/usr/bin/python3
import sys, subprocess
p = subprocess.Popen(["gsettings", "get", "org.gnome.desktop.background", "picture-uri"],stdout=subprocess.PIPE)
result = p.communicate(0)[0]
if (result == '') or (result.strip() == 'file:///usr/share/backgrounds/warty-final-ubuntu.png'):
 #user has not changed wallpaper'
 sys.exit(1)
else:
 #user has changed wallpaper'
 sys.exit(0)
