# Server manager!
# last commit: Mishqutin - master - whatever
from lib.config import *



class ServerManager:
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

        cmd, args = self.Shell.parseString(string)

        path = self.Shell.findCmd(cmd)

        if path != "": # Exists.
            # Run command.
            fname, ext = os.path.splitext(path)

            if ext == ".py":
                ret = self.Shell.run(path, args, cData)
            else:
                ret = self.Shell.runFile(path, args)

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










# eof
