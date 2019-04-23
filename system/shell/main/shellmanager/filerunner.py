# Run files multi-platform.
from main.config import *
import subprocess
import os

# Diffrent file exec code:
# "#@|/path/to/file"

def runFile(param):
    """param - list."""

    fname = param[0]
    if os.path.isfile(fname):
        f = open(fname)
        string = f.readline()
        f.close()

        if string[0:3] == "#@|":
            res = runFileOffset(param, string)
            return res

    res = subprocess.run(param, shell=False, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")

    return res


def runFileOffset(args, line):
    path = ROOT_PATH+line[3:-1]
    
    res = subprocess.run([path, *args], shell=False, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")
    return res
