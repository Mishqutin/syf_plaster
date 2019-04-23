Jajko Command Shell
==============================

## SYF PLASTER ECHO PASTA ERROR!!

#### TO-DO list

1. Add something like user system also whatever.

#### Holes

1. cmdproc.py line 49, function parseString:  
   Raises ValueError: no escaped character  
   when user sends "\\".

-----


Features:
* Lemonade
* Apple juice
* Don't be racist guys, racism is a crime and crime is for black people.


## Directory overview

`system/` - System core files required to work.  
`bin/` - Executable files (currently `.py` are considered such).  
`apps/` - Applications' files.  
`data/` - Applications' data.  
`home/` - User's home.  


### system directory

`system/apps/` - Core system's apps, providing basic operations.  
`system/bin/` - System's essential executable files (currently `.py` are considered such).  
`system/execlibs/` - Python modules safe to load via `exec` to global namespace.  
`system/shell/` - Core program's files.


`system/shell/client/` - Program used for input. Also imported by core. **Temporary location**.  
`system/shell/logs/` - Logs.  
`system/shell/main/` - Core modules.
`system/shell/init.py` - Init script, ran first.  
`system/shell/config.cfg` - Server config (IP etc.).


`system/shell/main/libs/` - Modules used by apps' functions (commands).  
`system/shell/main/server/` - Server module.  
`system/shell/main/shellmanager/` - Shell manager's required modules.  
`system/shell/main/config.py` - Config imported by other modules.  
`system/shell/main/serverman.py` - Server manager module.  
`system/shell/main/shellman.py` - Shell (manager) module.


### apps, data - directories structure

`apps/<app_name>/` - Your app's static files - it's code, modules.  
`data/<app_name>/` - Your app's dynamic files - e.g. config files, info generated about host, save games etc.


#### app files and commands
**Syntax described below may change in future.**

so you put e.g. dick.py in /bin and inside write:
```
def main(path, args, cData):
    return {"msg": 'daddys long purple throbbing dick'}
```
and yo have yo command then just write `dick` in console and yeah.


**For a good example, go die.**

#### cData - client's cData
TBD






----------


## Ignore everything down there

I EAT DUST.  
I EAT DUST.
JUST LIKE I ATE MY BANANAS.
I EAT DUST.
