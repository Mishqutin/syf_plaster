# Whole system core or so idk.
#
import os
import sys
import subprocess
import inspect

# Gotta switch to somethin' else soon, cos deprecated
import _thread as thread

from libs.cmdproc import CmdProcessor
from libs.server import server
from libs.os_shell import RunShell
from client.client import Client

from libs.shellmanager import ServerMan


# == CLASSES =================================================================

# SHELL FUNCTIONS.
class ShellMan:
    """Manages shell actions like loading new shit, shutdown etc.""" # TODO:Clean docstr.

    config = {}
    def loadConfig():
        """Load configuration file into ShellMan.config as dict type."""
        f = open(SYS_PATH+"/config.cfg", 'r')
        configStr = f.read()
        f.close()

        ShellMan.config = eval(configStr)


    def loadApp(path):         # Lol over 80 long docstr line what do? here V.
        """\
        Load application's <app>/shell/*.py files, execute them in global namespace
        and add and/or override returned commands in dict COMMANDS to
        Shell class (type: CommandProcessor).
        Return True if succeed, False if path not found.

        bool loadApp(path)
        str path -- Valid path to app.
                    Should be located in `/apps` or `/system/apps`

        """
        if os.path.isdir(path):
            if os.path.isdir(path+"/shell"): # If app has /shell dir.
                appShellDir = path+"/shell"

                for file in os.listdir(appShellDir):
                    fileExt = file[-3:]
                    if fileExt==".py": # Exec only .py files.
                        f = open(appShellDir+"/"+file, 'r')
                        code = f.read()
                        f.close()

                        execLocals = {
                            "ROOT_PATH": ROOT_PATH,
                            "APP_PATH": SYS_APPS_PATH+"/"+i,
                            "COMMANDS": {}
                        }
                        exec(code, globals(), execLocals)
                        # Add commands.
                        Commands = execLocals["COMMANDS"]
                        for name, func in Commands.items():
                            Shell.addCmd(name, func)

            return True
        else:
            return False

    def shutdown():
        """Shutdown system.
        Stop program loop and end main thread.

        Please use ShellMan.code(1) instead.
        """
        global Running

        print("Shutdown...")

        # Stop program loop.
        Running = False
        # Send last message to socket to 'wake' and close main thread.
        # See ServerAcceptHandler function before the eof.
        key = ShellMan.config["Server.Key"]
        port = ShellMan.config["Server.Port"]

        data = {"key": key, "name": "ShellMan.shutdown", "string": "ping"}
        ip = ("localhost", port)
        Client.connect(SERVER_IP, data)

    def code(n):
        """Execute certain shell action.

        None code(n)
        int n -- Code.
                 Raise a TypeError if n isn't int type.

        Negative values should be used only by system functions.
        Codes, positive:
         1 - Shutdown system.
        Codes, negative:
         -1 - Wrong directory structure error.
        """
        if type(n)!=int: raise TypeError("code argument must be of int type.")

        # Positive.
        if n==1: # 1 - shutdown
            ShellMan.shutdown()
        # Negative.
        elif n==-1: # -1 - wrong dir error
            ShellMan._fail_wrongPath()

    def _fail_wrongPath():
        errorMessage = """\
==Error==
>Wrong or renamed directory!
Please run `python shell.py` directly from it's directory.
If it doesn't help, it means that the file is in wrong directory
 or dir has been renamed.
Proper path to file should be:
 `system/shell/shell.py`"""

        print(errorMessage)
        input("-Press [Return] to dismiss-")
        # Exit with error.
        sys.exit(1)




# == CLASSES END =============================================================


# == INIT ====================================================================

# Path constants.
SYS_PATH = os.path.normpath( os.path.abspath(os.getcwd()+"/..") ) # /system
SYS_APPS_PATH = os.path.normpath( SYS_PATH+"/apps" )              # /system/apps
SYS_SHELL_PATH = os.path.normpath( SYS_PATH+"/shell" )            # /system/shell

ROOT_PATH = os.path.normpath( os.path.abspath(SYS_PATH+"/..") )         # /
ROOT_APPS_PATH = os.path.normpath( os.path.abspath(ROOT_PATH+"/apps") ) # /apps

if (not os.path.basename(SYS_PATH)=="system" # no /system
    or not os.path.basename(os.getcwd())=="shell"): # no ../shell
    ShellMan.code(-1) # Wrong directory structure.


# Load config file.
ShellMan.loadConfig()


# Init shell's command processor.
Shell = CmdProcessor()

# Load apps, commands -> Shell CmdProcessor.
for i in os.listdir(SYS_APPS_PATH): # /system/apps
    if os.path.isdir(SYS_APPS_PATH+"/"+i):
        ShellMan.loadApp(SYS_APPS_PATH+"/"+i)

for i in os.listdir(ROOT_APPS_PATH): # /apps
    if os.path.isdir(ROOT_APPS_PATH+"/"+i):
        ShellMan.loadApp(ROOT_APPS_PATH+"/"+i)


# Server config.
SERVER_KEY = ShellMan.config["Server.Key"]
SERVER_ADDRESS = ShellMan.config["Server.Address"]
SERVER_PORT    = ShellMan.config["Server.Port"]
SERVER_IP = (SERVER_ADDRESS, SERVER_PORT)
# Log path's static.
LOG_PATH = SYS_PATH+"/shell/logs/server.log"

# Init shell's server.
Server = server.Server(SERVER_IP, SERVER_KEY, log=True, logfile=LOG_PATH)


# Go home. See ya!
os.chdir(ROOT_PATH+"/home") # /home

# == INIT END ================================================================





# == PROGRAM LOOP ============================================================
print("Current working dir:", os.getcwd())
print(">Running<")

Running = True
while Running:
    Server.accept(ServerMan.serverAcceptHandler, closeClient=False)

print(">Quit.<")

# == PROGRAM LOOP END ========================================================


# EOF
