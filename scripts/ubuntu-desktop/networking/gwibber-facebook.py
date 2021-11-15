#!/usr/bin/python3
"""
Returns a list of services available as json string
"""
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import json
import sys
try:
    import gwibber.lib
    DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()
    gw = gwibber.lib.GwibberPublic()
    accounts = json.loads(gw.GetAccounts())
#go through json array picking up ALL services
    arrayServices = []
    i = 0
    for service in accounts:
        arrayServices.append(accounts[i]['service'])
    i = i +1
#make array contain only unique services
    tempArray = {}
    for x in arrayServices: tempArray[x] = 0
    arrayServices = tempArray.keys()
    if u'facebook' in arrayServices:
    #facebook setup on gwibber'
        sys.exit(0)
    else:
    #facebook not setup on gwibber'
        sys.exit(1)
except:
    sys.exit(2)
