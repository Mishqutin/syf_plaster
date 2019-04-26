# The Config!
# last commit: Mishqutin - master - 21.03.2019
import os
import sys
import subprocess
import inspect

# Gotta switch to somethin' else soon, cos deprecated
import _thread as thread

from main.libs.os_shell import RunShell
from main.libs.colors import Colors
from client.client import Client

# THE ALMIGHTY VlaD-PUTIN!





SYS_PATH = os.path.normpath( os.path.abspath(os.getcwd()+"/..") ) # /system

SYS_SHELL_PATH = os.path.normpath( SYS_PATH+"/shell" )            # /system/shell

ROOT_PATH = os.path.normpath( os.path.abspath(SYS_PATH+"/..") )         # /
PATH = ROOT_PATH

HOME_PATH = os.path.normpath( os.path.abspath(os.getcwd()+"/../../home") ) # /home



if os.name == "nt": # Repair functionality broken by NT system
    # not needed already ./bin/nigga works
    pass # os.environ["pathext"] += "; ;" # ;-;



# dict Settings - settings/flags for program.
Settings = {}
Settings["Running"] = True

Settings["config_file"] = PATH+"/system/etc/config.cfg"
f = open(Settings["config_file"], 'r')
Settings["config"] = eval(f.read())
f.close()

Settings["log_file"] = PATH+"/system/var/server_logs/server.log"

Settings["Shell.nocommand"] = "{cmd}: no such command."
Settings["Shell.x-perm-denied"] = "Permission denied for execution" # unused

Settings["Globals"] = {}




# eof nigga
