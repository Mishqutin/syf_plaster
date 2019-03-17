






def pwd(cmd, args, cData):
    return {"msg": os.getcwd()}
COMMANDS["pwd"] = pwd

def ls(cmd, args, cData):
    if len(args)>0:
        return {"msg": ', '.join(os.listdir(args[0]))}
    else:
        return {"msg": ', '.join(os.listdir())}
COMMANDS["ls"] = ls

def cd(cmd, args, cData):
    try:
        os.chdir(args[0])
    except Exception as e:
        return {"msg": str(e)}
COMMANDS["cd"] = cd

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
COMMANDS["cat"] = cat

def stat(cmd, args, cData):
    if len(args)==1:
        file = args[0]
        if os.path.isfile(file):
            msg = str(os.stat(file))
        else:
            msg = "stat: File not found"
        return {"msg": msg}
COMMANDS["stat"] = stat
