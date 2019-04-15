



def ping(cmd, args, cData):
    """Send Ping and receive Pong.
    Ping Pong!"""
    msg = "Pong"
    return {"msg": msg}
COMMANDS["ping"] = ping


def pong(cmd, args, cData):
    """pong: no such command"""
    msg = "Wait, that's illegal!"
    return {"msg": msg}
COMMANDS["pong"] = pong


def echo(cmd, args, cData):
    """Usage: echo <message>
    Echo message back to client."""
    return {"msg": ' '.join(args)}
COMMANDS["echo"] = echo

def consoleprint(cmd, args, cData):
    """Usage: print <message>
    Print message to host's console."""
    print(' '.join(args))
COMMANDS["print"] = consoleprint





def localname(cmd, args, cData):
    """Usage: localname
    Get your name."""
    return {"msg": cData["name"]}
COMMANDS["localname"] = localname
