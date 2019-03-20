# Init script!

from main.config import *
from main.shellman import ShellManager
from main.serverman import ServerManager

from libs.server import server


Shell = ShellManager(includeTestCmd=True)
Shell.loadConfig()

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

print("Server close")
Server.close()




print("eof")
# eof
