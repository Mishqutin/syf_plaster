

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





def localname(cmd, args, cData):
    return {"msg": cData["name"]}
commands["localname"] = localname











COMMANDS = commands
