from main.config import *



class ServerManager:
    """Functions used to operate shell's Server.
    -serverAcceptHandler(c, cData)
    -serverAccept(c, cData)"""

    def __init__(self, shell, shellmngr):
        self.Shell = shell
        self.ShellMan = shellmngr

    def serverAcceptHandler(self, c, cData):
        """Pass the client's request to a new thread and continue to the main loop."""
        if not Settings["Running"]: return # Server shutdown - quit. See ShellMan.shutdown.

        # Fulfill client's task in separate thread so main process can continue.
        thread.start_new_thread(self.serverAccept, (c, cData))
        # Continue to main loop.

    def serverAccept(self, c, cData): # TODO: Clean up, comment, etc.
        """Handle the client's request."""
        # cData - client data.
        # c - client socket.
        string = cData["string"] # Full command string.

        if not len(string.split()): return None # Empty string.

        if type(cData) == dict: # Success.
            cmdSplit = string.split()
            cmd = cmdSplit[0]

            if self.Shell.isCmd(cmd): # Cmd exists.
                # Run command.
                cmdString = cData["string"]
                ret = self.Shell.runString(cmdString, cData)

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
                c.send((cmd + ": command not found.").encode())

            return True
        else:                  # Client data syntax error.
            print("An error occured: " + cData)
            return False
        c.close()



# eof
