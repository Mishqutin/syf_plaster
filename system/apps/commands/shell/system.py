



# Clear and reload all apps and commands.
def reload(cmd, args, cData):
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
    global Running
    Running = False
    msg = "System shutdown."
    return {"msg": msg}
COMMANDS["shutdown"] = shutdown



# Stops thread execution for number of seconds
def sleep(cmd, args, cData):
    from time import sleep as tsleep
    if len(args)==0:
        msg = "sleep: syntax error"
    elif len(args)>=1:
        n = args[0]
        try:
            n = int(n)
        except:
            n = False
        if not n:
            msg = "sleep: first argument must be a number greater than 0"
        else:
            tsleep(n)
            msg = ' '.join(args[1:])
    return {"msg": msg}
COMMANDS["sleep"] = sleep
