




def reload(cmd, args, cData):
    """Reload all apps and commands."""
    Shell.COMMANDS = {}
    for i in os.listdir(SYS_APPS_PATH): # /system/apps.
        if os.path.isdir(SYS_APPS_PATH+"/"+i):
            ShellMan.loadApp(SYS_APPS_PATH+"/"+i)

    for i in os.listdir(ROOT_APPS_PATH): # /apps.
        if os.path.isdir(ROOT_APPS_PATH+"/"+i):
            ShellMan.loadApp(ROOT_APPS_PATH+"/"+i)
    return {"msg": "System reloaded."}
COMMANDS["reload"] = reload


def shutdown(cmd, args, cData):
    """Shutdown the system."""
    msg = "System shutdown."
    return {"msg": msg, "code": 1}
COMMANDS["shutdown"] = shutdown



def sleep(cmd, args, cData):
    """Usage: sleep <time> [<message>]
    Stop thread execution for a number of seconds.
    Optionally display message at the end."""
    from time import sleep as tsleep

    if len(args)==0:
        msg = "sleep: syntax error"
    elif len(args)>=1:
        n = args[0]
        try:
            n = int(n)
        except:
            n = False
        if not n or n<0:
            msg = "sleep: first argument must be a number greater than 0"
        else:
            tsleep(n)
            msg = ' '.join(args[1:])
    return {"msg": msg}
COMMANDS["sleep"] = sleep
