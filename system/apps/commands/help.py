# Commands providing help etc.
#



def help(cmd, args, cData):  # TODO: Clean up.
    """Usage: help <command>
    Shows documentation for a command if available"""
    if len(args)==1:
        command = args[0]
        if Shell.Cmd.isCmd(command):
            doc = Shell.Cmd.commands[command].__doc__
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


def listcmd(cmd, args, cData):
    """Show all available commands."""
    msg = ', '.join(Shell.Cmd.commands)
    return {"msg": msg}
COMMANDS["listcmd"] = listcmd
