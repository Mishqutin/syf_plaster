from main.config import *
from shlex import split as shlex_split


class CmdProcessor:

    def __init__(self):
        pass

    def run(self, path, args, *argsv):
        f = open(path, 'r')
        code = f.read()
        f.close()

        execGlobals = globals()
        execLocals = {
            "command": None
        }
        exec(code, execGlobals, execLocals)

        func = execLocals["command"].main

        return func(path, args, *argsv)

    def runString(self, string, *argsv):
        if len(shlex_split(string))<1: return

        name = shlex_split(string)[0] #.lower()
        args = shlex_split(string)[1:]

        path = self.findCmd(name)
        if type(path)!=str: raise TypeError("findCmd returned non-str")

        return self.run(path, args, *argsv)

    def isCmd(self, name):
        if type(self.findCmd(name))==str: return True
        else: return False

    def findCmd(self, name):
        path = None
        for app in os.listdir(SYS_APPS_PATH): # /system/apps
            if os.path.isdir(SYS_APPS_PATH+"/"+app+"/shell"): # If app has /shell dir.
                appShellDir = SYS_APPS_PATH+"/"+app+"/shell"
                if name+'.py' in os.listdir(appShellDir):
                    path = appShellDir+"/"+name+'.py'
                    return path

        for app in os.listdir(ROOT_APPS_PATH): # /apps
            if os.path.isdir(ROOT_APPS_PATH+"/"+app+"/shell"): # If app has /shell dir.
                appShellDir = ROOT_APPS_PATH+"/"+app+"/shell"
                if name+'.py' in os.listdir(appShellDir):
                    path = appShellDir+"/"+name+'.py'
                    return path

        return False
