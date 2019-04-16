from main.config import *
from shlex import split as shlex_split


class CmdProcessor:

    def __init__(self):
        self.variables = {}

        bin1 = ROOT_PATH+"/bin"
        bin2 = SYS_PATH+"/bin"
        self.setVar("path",
            bin1+":"+bin2
        )

    # Variable functions.
    def setVar(self, key, value):
        keytype = type(key)
        if keytype != str:
            raise TypeError("expected 'key' of type str but got "+str(keytype))
        else:
            self.variables[key.lower()] = value

    def readVar(self, key):
        return self.variables[key.lower()]

    def isVar(self, key):
        return key.lower() in self.variables

    # Command functions.
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

    def parseString(self, string):
        if len(shlex_split(string))<1: return ()

        name = shlex_split(string)[0] #.lower()
        args = shlex_split(string)[1:]

        return (name, args)

    def isCmd(self, name):
        if type(self.findCmd(name))==str: return True
        else: return False

    def findCmd(self, name):
        pathList = self.readPath()

        if name[0] == "/" or name[0:2] == "./":
            if os.path.isfile(name):
                res = name
            else:
                res = ""

            return res
        else:
            res = ""
            for path in pathList:
                res = self.searchPath(name, path)
                if res != "": break

            return res



    def searchPath(self, name, path):
        filepath = path+"/"+name
        if os.path.isfile(filepath):
            return filepath
        elif os.path.isfile(filepath+".py"):
            return filepath+".py"
        else:
            return ""

    def readPath(self):
        return self.readVar("path").split(":")

    def findCmd_stage1(self, name):
        for app in os.listdir(SYS_APPS_PATH): # /system/apps
            if os.path.isdir(SYS_APPS_PATH+"/"+app+"/shell"): # If app has /shell dir.
                appShellDir = SYS_APPS_PATH+"/"+app+"/shell"
                if name+'.py' in os.listdir(appShellDir):
                    path = appShellDir+"/"+name+'.py'
                    return path

    def findCmd_stage2(self, name):
        for app in os.listdir(ROOT_APPS_PATH): # /apps
            if os.path.isdir(ROOT_APPS_PATH+"/"+app+"/shell"): # If app has /shell dir.
                appShellDir = ROOT_APPS_PATH+"/"+app+"/shell"
                if name+'.py' in os.listdir(appShellDir):
                    path = appShellDir+"/"+name+'.py'
                    return path

    def findCmd_stage3(self, name):
        pass
