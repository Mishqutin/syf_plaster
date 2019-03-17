
commands = {}

def ziprun(cmd, args, cData):
    APP = ROOT_APPS_PATH+"/ziprun"
    FILE = APP+"/ziprun.py"

    if len(args)!=1:
        msg = "Usage: ziprun <path-to-file>"
        return {"msg": msg}


    msg = RunShell(["python", FILE, args[0], "{'ROOT_PATH': '"+ROOT_PATH.replace("\\", "/")+"'}"], errContinue=True)

    if type(msg)!=str: msg = str(msg)
    return {"msg": msg}
commands["ziprun"] = ziprun

COMMANDS = commands
