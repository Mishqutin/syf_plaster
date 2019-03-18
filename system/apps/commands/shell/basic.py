



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



def help(cmd, args, cData):
    """Usage: help <command>"""
    if len(args)==1:
        command = args[0]
        if Shell.isCmd(command):
            doc = Shell.commands[command].__doc__
            if doc!=None:
                msg = "\n"+inspect.cleandoc(doc)
            else:
                msg = "help: Command does not provide documentation."
        else:
            msg = "help: No such command."
    else:
        msg = """\
help: syntax error.
Usage: help <command>"""
    return {"msg": msg}
COMMANDS["help"] = help
