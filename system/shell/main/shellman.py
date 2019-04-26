# Shell Manager!
# last commit: Mishqutin - master - who cares
from main.config import *
from main.shellmanager.cmdproc import CmdProcessor




class ShellManager:
    """Shell Manager"""

    # INIT STUFF ========
    def __init__(self):
        
        # Command Processor.
        print("[i]shell: command processor")
        self.Cmd = CmdProcessor()
        # Binds.
        #run = self.Cmd.run
        #runString = self.Cmd.runString

        


    # INIT STUFF END ====




    def code(self, n):
        """Execute certain action.

        None code(n)
        int n -- Code.
                 Raise a TypeError if n isn't int type.

        Negative values should be used only by system functions.
        Codes, positive:
         1 - Shutdown system.
        Codes, negative:
         -1 - wtf.
        """
        if type(n)!=int: raise TypeError("code argument must be of int type.")

        # Positive.
        if n==1: # 1 - shutdown
            self.shutdown()
        # Negative.
        elif n==-1: # -1 - currently nothing
            print("Jebać psy!")


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








# eof everywhere cos I need place
