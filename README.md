Jajko Command Shell
==============================

## SYF PLASTER ECHO PASTA ERROR!!
































## Ignore everything down there

/apps - Applications' static files required to work.
/apps/<app> - Your app's files.
/apps/<app>/shell - Files loaded by shell at start.

/apps/<app>/shell/<file>.py -
    Files here with '.py' extension are runned at the start of the system.
    From each file variable 'COMMANDS' (type: dict) is kept and commands
    from there are loaded. Keys (strings) are the names of the commands
    and values (functions) are their functions.

Command functions:
nigga idk. But if yo put in return {"msg": "hello"}
it will send hello to the client mothafucka.


/data - Applications' variable files (that can change at some point).
/data/<app> - Your app's stuff.


/system - Files required for system to work.
/system/apps - Same as /apps but vital for system. Don't put anything there.
/system/execlibs - .py libraries safe to be run by `exec` in order to be loaded.
/system/shell - System shell.


/home - Users' home directory.


/README.md - Essential file for uhhhhh i dunno gtfo





To create a new command:

1.Put a file in /apps/<app>/shell. Must have .py extension.

2.Now write a new function how you want your command to work.
  Must have 3 arguments: cmd, args, cData.
  string cmd - Your commands name. Useful if same function is used for several commands.
  list args - List of arguments (strings) passed.
  dict cData - Client data. I ain't gonna fuck with this here.

4.After you're done with yo func, store it in dict
  called COMMANDS, e.g. COMMANDS["name_of_mah_func"] = func

Yay you're done. Take a look also how's it done in /system/apps.
