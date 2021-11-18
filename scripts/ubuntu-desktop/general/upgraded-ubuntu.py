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
    install_release = release_info[1].strip()
    f.close()
    # get current release
    f = open('/etc/lsb-release', 'r')
    if not f:
        sys.exit(1)
    current_relinfo = f.read().splitlines()
    current_release = None
    for release_line in current_relinfo:
        parts = release_line.split('=')
        if len(parts) == 2 and parts[0].strip() == 'DISTRIB_RELEASE':
            current_release = parts[1].strip()
            break
    if current_release is None or current_release == '':
        sys.exit(1)

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
