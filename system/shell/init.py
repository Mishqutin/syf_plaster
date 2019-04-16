# Init script!
# last commit: Mishqutin - master - i dunno
from main.config import *

from main.shellman import ShellManager
from main.serverman import ServerManager

from main.server import server

Settings["Globals"] = globals()

print("Init Shell (Manager).")
Shell = ShellManager()


print("Init Server Manager.")
ServerMan = ServerManager(Shell.Cmd, Shell)

# Server config.
print("Server config")
SERVER_KEY = Shell.config["Server.Key"]
SERVER_ADDRESS = Shell.config["Server.Address"]
SERVER_PORT    = Shell.config["Server.Port"]
SERVER_IP = (SERVER_ADDRESS, SERVER_PORT)
# Log path's static.
LOG_PATH = SYS_PATH+"/shell/logs/server.log"

# Init shell's server.
print("Server start")
Server = server.Server(SERVER_IP, SERVER_KEY, log=True, logfile=LOG_PATH)

os.chdir(HOME_PATH)

print("Init done!")
print(os.getcwd())
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
