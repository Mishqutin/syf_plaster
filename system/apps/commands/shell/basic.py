



def ping(cmd, args, cData):
    """Send Ping and receive Pong.
    Ping Pong!"""
    msg = "Pong"
    return {"msg": msg}
COMMANDS["ping"] = ping
COMMANDS["Ping"] = ping

def pong(cmd, args, cData):
    """Command doesn't exist."""
    msg = "Wait, that's illegal!"
    return {"msg": msg}
COMMANDS["pong"] = pong
COMMANDS["Pong"] = pong

def echo(cmd, args, cData):
    """echo <message>

    Echo message back to client."""
    return {"msg": ' '.join(args)}
COMMANDS["echo"] = echo

def consoleprint(cmd, args, cData):
    """print <message>

    Print message to host's console."""
    print(' '.join(args))
COMMANDS["print"] = consoleprint





def localname(cmd, args, cData):
    """localname

    Get your name."""
    return {"msg": cData["name"]}
COMMANDS["localname"] = localname
