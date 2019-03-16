from shlex import split as shlex_split


class CmdProcessor:
    
    def __init__(self, commands={}):
        self.commands = commands
    
    def run(self, cmd, args, *argsv):
        return self.commands[cmd](cmd, args, *argsv)
    
    def runString(self, string, *argsv):
        if len(shlex_split(string))<1: return
        
        cmd = shlex_split(string)[0]
        args = shlex_split(string)[1:]
        
        return self.commands[cmd](cmd, args, *argsv)
    
    def addCmd(self, name, func):
        self.commands[name]=func
    
    def isCmd(self, name):
        if name in self.commands: return True
        else: return False