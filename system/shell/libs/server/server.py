from datetime import datetime
import socket
import ast






class Server:
    
    def __init__(self, IP, key, log=False, logfile="./server_log"):
        """\
tuple IP: (str address, int port) - Server's address.
str key - Server's key/password.
bool log - Enable logging to file? default: False
str logfile - Path to file where log will be written. default: "./server_log" """
        self.IP  = IP
        self.KEY = key
        
        self.Log = log
        self.LogFile = logfile
        
        self.s = socket.socket()
        self.s.bind(self.IP)
        self.s.listen(1)
        
        self.log("Server start\n====================Server start====================", "\n")
    
    
    def newKey(self, key):
        """Change server's key."""
        self.KEY = key
        self.log("[!] Changed server's key.")
    
    
    
    
    def log(self, msg, sep=""):
        """\
Append log if enabled.
str msg - Message to write.
str sep - String separating entry from others. default: "" """
        if not self.Log: return
        
        txt = sep + datetime.strftime(datetime.now(), "%Y %B %d, %H:%M:%S > ") + str(msg) + "\n"
        f = open(self.LogFile, 'a')
        f.write(txt)
        f.close()
    
    
    
    def accept(self, func, funcArgs=[], closeClient=True):
        """\
Await connection, validate client and execute given function.
Arguments:
  function func - Function to call after validation.
  list funcArgs - Function `func` parameters (default: []).
  bool closeClient - Close client socket after function return? (default: True).

Function `func` is called with following parameters:
  func(c, cData, funcArgs[0], funcArgs[1], ...)
  
  socket c - Client's socket.
  dict cData - Client's data.
  elements from list `funcArgs` if present.


If client's data is valid return data (type dict) and client's socket.
If an error occured return string and client's socket:
  "data_corrupted" - Data couldn't be read.
  "data_missing" - Data misses keys ("key", "name" or "command" aren't present).
  "wrong_key" - Data key differs from server.
"""
        c, cAddress = self.s.accept()
        
        funcReturn = None
        
        self.log("Connection from: " + str(cAddress) + ".", "\n") # Log.
        
        
        try: # Decode client message. Has to be a dict type.
            cData = ast.literal_eval( (c.recv(65536)).decode("UTF-8") )
        except: # Client data corrupted.
            c.close()
            self.log("[Error] Received corrupted data (exception).")
            if func: funcReturn = func(c, "data_corrupted", *funcArgs)
            return "data_corrupted", c, funcReturn
        
        
        
        # Data is not a dictionary.
        if not type(cData) == dict:
            c.close()
            self.log("[Error] Received corrupted data (not dict type).")
            if func: funcReturn = func(c, "data_corrupted", *funcArgs)
            return "data_corrupted", c, funcReturn
        
        self.log("Received data: " + str(cData) + ".")
        
        # Data missing required entries.
        if not ("key" in cData and "name" in cData and "string" in cData):
            c.close()
            self.log("[Error] Received data with missing keys.")
            if func: funcReturn = func(c, "data_missing", *funcArgs)
            return "data_missing", c, funcReturn
        
        # Data with invalid key.
        if not cData["key"] == self.KEY:
            c.close()
            self.log("[Error] Received invalid key.")
            if func: funcReturn = func(c, "wrong_key", *funcArgs)
            return "wrong_key", c, funcReturn
        
        
        self.log("[OK] Data validated.")
        
        # Call given function with arguments.
        if func: funcReturn = func(c, cData, *funcArgs)
        
        
        if closeClient: c.close()
        
        return cData, c, funcReturn
    
    
    
    
    
    def close(self):
        """Close server."""
        self.s.close()
    



if __name__=="__main__":
    
    def myFunc(c, cData, prefix):
        if type(cData) == dict: # If received dict
            print(prefix, cData["string"])
            return "Success"
        else:                  # If not dict: string with error
            print(prefix, "An error occured: " + cData)
            return "Error"
    
    SERVER_IP  = ("localhost", 12345)
    SERVER_KEY = "chujnia"
    #                    IP          KEY    [Log? default: False]
    myServer = Server(SERVER_IP, SERVER_KEY, True)

    while True:
        data, c, msg = myServer.accept(myFunc, ["im jeff: "])
        print("myFunc:", msg)



