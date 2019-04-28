# The Config!
# last commit: Mishqutin - master - 21.03.2019
import os
import sys
import subprocess
import inspect

# Gotta switch to somethin' else soon, cos deprecated
import _thread as thread

from lib.python.os_shell import RunShell
from lib.python.colors import Colors
from lib.python.client import Client

# THE ALMIGHTY VlaD-PUTIN!





ROOT_PATH = os.getcwd() # /
PATH = ROOT_PATH



if os.name == "nt": # Repair functionality broken by NT system
    # not needed already ./bin/nigga works
    pass # os.environ["pathext"] += "; ;" # ;-;



# dict Settings - settings/flags for program.
Settings = {}
Settings["Running"] = True

Settings["config_file"] = PATH+"/etc/config.cfg"
f = open(Settings["config_file"], 'r')
Settings["config"] = eval(f.read())
f.close()

Settings["log_file"] = PATH+"/var/server_logs/server.log"

Settings["Shell.nocommand"] = "{cmd}: no such command."
Settings["Shell.x-perm-denied"] = "Permission denied for execution" # unused

Settings["Globals"] = {}




# eof nigga
