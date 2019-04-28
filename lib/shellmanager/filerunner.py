# Run files multi-platform.
from lib.config import *
import subprocess
import os

# Diffrent file exec code:
shebang = "#@#" # "@#" - at 'root' of this program.


def runFile(args):
    """args - list."""

    
    filename = args[0]
    if filename[0] == ".":
        filename = os.getcwd() + filename[1:]
        args[0] = filename
        
    if os.path.isfile(filename):
        try:
            f = open(filename, 'r')
            cfgline = f.readline().replace("\n", "") # Strip trailing \n
            f.close()
        except: # Couldn't read - it's binary.
            return runFileDirect(args)
        
        
        
        if False: # Skip permission check 'cos tbd.
            pass # check permissions.

        runType = checkHowToRun(args, filename, cfgline) #

        if runType == 1:
            res = runFileCustom(args, filename, cfgline)
        else:
            res = runFileDirect(args)

        return res
    
    else:
        return "No such file."


def runFileDirect(args):
    res = subprocess.run(' '.join(args), shell=True, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")
    return res

def runFileCustom(args, filename, cfgline):    
    if cfgline[0:2] == "#!":
        startwith = cfgline[2:]
    elif cfgline[0:3] == "#@#":
        startwith = ROOT_PATH+cfgline[3:]
    else:
        startwith = None
        raise ValueError("File's 1st line doesn't contain any of the following ('#!', '{}')".format(shebang))

    finalArgs = [startwith, *args]
    res = runFileDirect(finalArgs)
    
    return res

def checkHowToRun(args, filename, cfgline):
    if cfgline[0:3] == "#@#":
        # If file has to be run with program from ROOT_PATH/*
        return 1
    elif os.name == "nt" and cfgline[0:2] == "#!":
        # If running on MS-DOS and file has to be run with program from /*
        return 1
    else:
        # If file has '#!' and running on GNU/Linux,
        # or doesn't have any start parameter and running on MS-DOS.
        return 0


# A random thought:
# Niggas makin' smartphones and systems for 'em could make some models
# with Debian or whatever distro and that would make my life easier
# 10/10 would loose money on such masterpieces.
