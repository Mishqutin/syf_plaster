

class command:
    def main(path, args, cData):
        """List current directory elements."""
        if len(args)>0: p = args[0]
        else: p = "."
        
        
        s = ""
        for i in os.listdir(p):
            file = p+"/"+i
            if os.path.isdir(file):
                app = Colors.blue+i+Colors.reset
            else:
                app = i
            s+= app+" "
        
        print(s)
        return {"msg": s}
    
