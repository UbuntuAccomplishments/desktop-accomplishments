#!/usr/bin/python3
import traceback, sys
import subprocess
try:
    # get architecture
    arch = subprocess.check_output(['uname', '-i'],
        universal_newlines=True)
    # get cpu hardware info
    f = open('/proc/cpuinfo','r')
    if not f:
        sys.exit(1)
    is_grouper = False
    for line in f:
        if line.startswith("Hardware"):
            field, value = line.split(":")
            if value.strip() == "grouper":
                is_grouper = True
                break
    if arch.strip() == "armv7l" and is_grouper:
        sys.exit(0)
    else:
        sys.exit(1)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
