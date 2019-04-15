

class command:
    def main(path, args, cData):
        """Usage: cat <file>
        Concatenate file to client's socket.
        There's a limit of file size: 8192B"""
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
