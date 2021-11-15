#!/usr/bin/python3
import traceback, sys
import subprocess
try:
    # get install media release version
    f = open('/var/log/installer/media-info','r')
    if not f:
        sys.exit(1)
    media_info = f.read()
    release_info = media_info.split()
    install_release = release_info[1]
    # get current release
    out = subprocess.check_output(['lsb_release', '-r'],
        universal_newlines=True).strip().decode('utf-8')
    _, current_release = out.split(":")
    current_release = current_release.strip()
    install_release = install_release.strip()
    # we need to strip off the LTS support release numbers or it will
    # confuse the float() call below.  So we go from 12.04.1 to 12.04
    rel = current_release.split('.')
    current_release = "%s.%s" % (rel[0], rel[1])
    rel = install_release.split('.')
    install_release = "%s.%s" % (rel[0], rel[1])
    current = float(current_release)
    install = float(install_release)
    if current > install:
        sys.exit(0)
    else:
        sys.exit(1)
except SystemExit as e:
    sys.exit(e.code)
except:
    traceback.print_exc()
    sys.exit(2)
