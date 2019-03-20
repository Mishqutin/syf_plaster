# Shell Manager!
from main.config import *
from main.shellmanager.cmdproc import CmdProcessor




class ShellManager:
    """Shell Manager"""

    # INIT STUFF ========
    def __init__(self, includeTestCmd=False):
        # Config.
        print("[i]shell: config...")
        self.config = {}
        self.loadConfig()

        # Command Processor.
        print("[i]shell: command processor")
        self.Cmd = CmdProcessor()
        # Binds.
        run = self.Cmd.run
        runString = self.Cmd.runString

        if includeTestCmd:
            print("[i]shell: including test cmds")
            self.Cmd.addCmd("test", self.shellTestCommand)


    # Load config file.
    def loadConfig(self):
        """Load configuration file 'system/config.cfg' to self.config."""
        f = open(SYS_PATH+"/config.cfg", 'r')
        configStr = f.read()
        f.close()

        self.config = eval(configStr)



    # Predefined test command, see above - __init__.
    def shellTestCommand(self, cmd, args, cData):
        print(" Shell Test Command")
        msg = "You have ran a Shell Test Command."
        return {"msg": msg}




    # INIT STUFF END ====












    def code(self, n):
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
            self.shutdown()
        # Negative.
        elif n==-1: # -1 - wrong dir error
            self._fail_wrongPath()


    def shutdown(self):
        """Shutdown system.
        Stop program loop and end main thread.

        Please use self.code(1) instead.
        I don't know why.
        """
        global Settings
        print("Shutdown...")

        # Stop program loop.
        Settings["Running"] = False
        # Send last message to socket to 'wake' and close main thread.
        # See ServerAcceptHandler function before the eof.
        key = self.config["Server.Key"]
        port = self.config["Server.Port"]

        data = {"key": key, "name": "shell.shutdown", "string": "ping"}
        ip = ("localhost", port)
        Client.connect(ip, data)

    # vvvv Down there i dunno just mess vvvvv

    def loadApp(self, path):         # Lol over 80 long docstr line what do? here V.
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
                            "APP_PATH": SYS_APPS_PATH+"/"+file,
                            "COMMANDS": {}
                        }
                        exec(code, globals(), execLocals)
                        # Add commands.
                        Commands = execLocals["COMMANDS"]
                        for name, func in Commands.items():
                            self.Cmd.addCmd(name, func)

            return True
        else:
            return False

    def _fail_wrongPath(self):
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







# eof everywhere cos I need place
