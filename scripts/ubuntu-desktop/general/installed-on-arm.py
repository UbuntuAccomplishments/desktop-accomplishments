#!/usr/bin/python3
import traceback, sys
import subprocess
try:
    # get architecture
    out = subprocess.check_output(['uname', '-i'],
        universal_newlines=True).strip()
    if out.startswith("arm") or out.startswith("aarch"):
        sys.exit(0)
    else:
        sys.exit(1)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
