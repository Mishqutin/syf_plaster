

commands = {}

def ping(cmd, args, cData):
    return {"msg": "Pong"}
commands["ping"] = ping

def echo(cmd, args, cData):
    return {"msg": ' '.join(args)}
commands["echo"] = echo

def conEcho(cmd, args, cData):
    print(' '.join(args))
commands["conEcho"] = conEcho


def pwd(cmd, args, cData):
    return {"msg": os.getcwd()}
commands["pwd"] = pwd

def ls(cmd, args, cData):
    if len(args)>0:
        return {"msg": ', '.join(os.listdir(args[0]))}
    else:
        return {"msg": ', '.join(os.listdir())}
commands["ls"] = ls

def cd(cmd, args, cData):
    try:
        os.chdir(args[0])
    except Exception as e:
        return {"msg": str(e)}
commands["cd"] = cd

def cat(cmd, args, cData):
    if len(args)==1:
        file = args[0]
        if os.path.isfile(file):
            if os.stat(file).st_size < 8192:
                f = open(file, 'r')
                msg = f.read()
                f.close()
            else:
                msg = "cat: Cannot concatenate. File too large."
        else:
            msg = "cat: File not found"
        return {"msg": msg}
commands["cat"] = cat

def stat(cmd, args, cData):
    if len(args)==1:
        file = args[0]
        if os.path.isfile(file):
            msg = str(os.stat(file))
        else:
            msg = "stat: File not found"
        return {"msg": msg}
commands["stat"] = stat


def localname(cmd, args, cData):
    return {"msg": cData["name"]}
commands["localname"] = localname

# Clear and reload all apps and commands.
def reload(cmd, args, cData):
    Shell.commands = {}
    for i in os.listdir(SYS_APPS_PATH): # /system/apps.
        if os.path.isdir(SYS_APPS_PATH+"/"+i):
            ShellMan.loadApp(SYS_APPS_PATH+"/"+i)

    for i in os.listdir(ROOT_APPS_PATH): # /apps.
        if os.path.isdir(ROOT_APPS_PATH+"/"+i):
            ShellMan.loadApp(ROOT_APPS_PATH+"/"+i)
    return {"msg": "System reloaded."}
commands["reload"] = reload



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
commands["sleep"] = sleep









COMMANDS = commands
