# The Config!
# last commit: Mishqutin - master - 20.03.2019
import os
import sys
import subprocess
import inspect

# Gotta switch to somethin' else soon, cos deprecated
import _thread as thread

from main.libs.os_shell import RunShell
from client.client import Client

# THE ALMIGHTY VlaD-PUTIN!




SYS_PATH = os.path.normpath( os.path.abspath(os.getcwd()+"/..") ) # /system
SYS_APPS_PATH = os.path.normpath( SYS_PATH+"/apps" )              # /system/apps
SYS_SHELL_PATH = os.path.normpath( SYS_PATH+"/shell" )            # /system/shell

ROOT_PATH = os.path.normpath( os.path.abspath(SYS_PATH+"/..") )         # /
ROOT_APPS_PATH = os.path.normpath( os.path.abspath(ROOT_PATH+"/apps") ) # /apps


# dict Settings - settings/flags for program.
Settings = {}
Settings["Running"] = True

Settings["Shell.nocommand"] = "{cmd}: no such command."






# eof nigga
