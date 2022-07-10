import os
import subprocess


def force_into(dist):
    try:
        os.chdir(dist)
    except:
        return False
    cd = os.popen('cd').read()[:-1]
    if str(cd) == str(dist):
        return True
    return False


