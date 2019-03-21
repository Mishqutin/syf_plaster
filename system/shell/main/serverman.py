# Server manager!
# last commit: Mishqutin - master - 21.03.2019
from main.config import *



class ServerManager: # TODO: CLEAN UP THIS SHIT!!!!!!
    """Functions used to operate shell's Server.
    -serverAcceptHandler(c, cData)
    -serverAccept(c, cData)"""

    def __init__(self, shell, shellmngr):
        self.Shell = shell
        self.ShellMan = shellmngr

    def serverAcceptHandler(self, c, cData):
        """Pass the client's request to a new thread and continue to the main loop."""
        if not Settings["Running"]: return # Server shutdown.

        if not type(cData)==dict:
            print("Broken client data.")
            c.close()

        # Fork to a new thread.
        thread.start_new_thread(self.serverAccept, (c, cData))
        # Continue to main loop.


    def serverAccept(self, c, cData):
        """Handle request."""
        string = cData["string"]

        if not len(string.split()): # Empty command.
            c.close()
            return

        self.processCommand(c, cData)

        c.close()


    def processCommand(self, c, cData):
        """Process command."""
        string = cData["string"]

        splitStr = string.split()
        cmd = splitStr[0]

        if self.Shell.isCmd(cmd): # Exists.
            # Run command.
            ret = self.Shell.runString(string, cData)

            self.processReturn(c, cData, ret)

            return True
        else: # Does not exist.
            msg = Settings["Shell.nocommand"]
            msg = msg.replace("{cmd}", cmd)

            c.send(msg.encode())

            return False


    def processReturn(self, c, cData, ret):
        """Process command's return value."""

        if type(ret)==dict:
            if "msg" in ret:
                # "msg" - message for client.
                msg = str(ret["msg"])
                c.send(msg.encode())
            if "code" in ret:
                # "code" - certain shell action.
                code = ret["code"]
                self.ShellMan.code(code)











    def processCommandGTFO(self, c, cData):
        string = cData["string"]

        cmdSplit = string.split()
        cmd = cmdSplit[0]
        if self.Shell.isCmd(cmd): # Cmd exists.
            # Run command.
            ret = self.Shell.runString(string, cData)

            if type(ret)==dict:
                if "msg" in ret:
                    # "msg" - message for client.
                    msg = str(ret["msg"])
                    c.send(msg.encode())
                if "code" in ret:
                    # "code" - certain shell action.
                    code = ret["code"]
                    self.ShellMan.code(code)
        else:
            msg = Settings["Shell.nocommand"]
            msg = msg.replace("{cmd}", cmd)
            c.send(msg.encode())








    def serverAcceptGTFO(self, c, cData): # TODO: Clean up, comment, etc.
        """Handle the client's request."""
        # cData - client data.
        # c - client socket.
        string = cData["string"] # Full command string.

        if not len(string.split()): return None # Empty string.

        if type(cData) == dict: # Success.
            self.processCommand(c, cData)
            return True
        else:                  # Client data syntax error.
            print("An error occured: " + cData)
            return False
        c.close()




# eof
