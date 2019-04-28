# Init script!
# last commit: Mishqutin - master - i dunno
from lib.config import *

from lib.shellman import ShellManager
from lib.serverman import ServerManager

from lib.jserver import server

Settings["Globals"] = globals()


print("Init Shell (Manager).")
Shell = ShellManager()


print("Init Server Manager.")
ServerMan = ServerManager(Shell.Cmd, Shell)

# Server config.
print("Server config")
SERVER_KEY     = Settings["config"]["Server.Key"]
SERVER_ADDRESS = Settings["config"]["Server.Address"]
SERVER_PORT    = Settings["config"]["Server.Port"]
SERVER_IP = (SERVER_ADDRESS, SERVER_PORT)
# Log path's static.
LOG_PATH = Settings["log_file"]

# Init shell's server.
print("Server start")
Server = server.Server(SERVER_IP, SERVER_KEY, log=True, logfile=LOG_PATH)

os.chdir(ROOT_PATH+"/home")

print("Init done!")
print("Log file @ "+LOG_PATH)
print("Currently @ "+os.getcwd())
print("Running")

while Settings["Running"]:
    try:
        Server.accept(ServerMan.serverAcceptHandler, closeClient=False)
    except KeyboardInterrupt:
        break



print("Server close")
Server.close()

print("eof")
# eof
