import os
import sys
import subprocess


import _thread as thread

from libs.cmdproc import CmdProcessor
from libs.server import server
from libs.os_shell import RunShell




# Constants
SYS_PATH = os.path.normpath( os.path.abspath(os.getcwd()+"/..") )
SYS_SHELL_PATH = os.path.normpath( SYS_PATH+"/shell" )
SYS_APPS_PATH = os.path.normpath( SYS_PATH+"/apps" )

ROOT_PATH = os.path.normpath( os.path.abspath(SYS_PATH+"/..") )
ROOT_APPS_PATH = os.path.normpath( os.path.abspath(ROOT_PATH+"/apps") )

# If path's wrong show a sad message.
if not os.path.basename(SYS_PATH)=="system" or not os.path.basename(os.getcwd())=="shell":
    print("==Error==")
    print(">Wrong or renamed directory!")
    print("Please run `python shell.py` or `shell.bat` directly from it's directory.")
    print("If it doesn't help, it means that the file is in wrong directory")
    print(" or dir has been renamed.")
    print("Proper path to file should be:")
    print("  `system/shell/shell.py`")
    input("-Press [Enter] to dismiss-")
    sys.exit(1)


# Command processor.
Shell = CmdProcessor()

# Shell manager.
class ShellMan:

    def loadApp(path):
        if os.path.isdir(path+"/shell"):
            appShellDir = path+"/shell"
            for file in os.listdir(appShellDir):
                if file[-3:]==".py":
                    f = open(appShellDir+"/"+file, 'r')
                    code = f.read()
                    f.close()

                    execLocals = {
                        "ROOT_PATH": ROOT_PATH,
                        "APP_PATH": SYS_APPS_PATH+"/"+i,
                        "COMMANDS": {}
                    }

                    exec(code, globals(), execLocals)

                    Commands = execLocals["COMMANDS"]

                    for name, func in Commands.items():
                        Shell.addCmd(name, func)



# == Load apps, commands ================================

for i in os.listdir(SYS_APPS_PATH): # /system/apps.
    if os.path.isdir(SYS_APPS_PATH+"/"+i):
        ShellMan.loadApp(SYS_APPS_PATH+"/"+i)

for i in os.listdir(ROOT_APPS_PATH): # /apps.
    if os.path.isdir(ROOT_APPS_PATH+"/"+i):
        ShellMan.loadApp(ROOT_APPS_PATH+"/"+i)




# == END ========================================================================================




# == SERVER CONFIG ===============================================
SERVER_IP  = ("localhost", 12345)
SERVER_KEY = "123456"

def serverAcceptHandler(c, cData):
    thread.start_new_thread(serverAccept, (c, cData))

def serverAccept(c, cData):
    if type(cData) == dict: # Success.
        pre_cmd = cData["string"].split()
        if len(pre_cmd) > 0:
            cmd = pre_cmd[0]

            if Shell.isCmd(cmd):
                ret = Shell.runString(cData["string"], cData)
                if type(ret)==dict:
                    if "msg" in ret: c.send(ret["msg"].encode())
            else:
                c.send("no such command".encode())
            return True
        else:
            return False

    else:                  # Syntax error.
        print("An error occured: " + cData)
        return False
    c.close()


Server = server.Server(SERVER_IP, SERVER_KEY, log=True, logfile=SYS_PATH+"/shell/logs/server.log")

# == END =========================================================

# cd home.
os.chdir(ROOT_PATH+"/home")



# Program loop.

while True:
    Server.accept(serverAcceptHandler, closeClient=False)
