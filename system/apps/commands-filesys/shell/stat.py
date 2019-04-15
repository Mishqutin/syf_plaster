

class command:
    def main(path, args, cData):
        """Usage: stat <file>
        Show file stats in some fucked up syntax."""
        if len(args)==1:
            file = args[0]
            if os.path.isfile(file):
                msg = str(os.stat(file))
            else:
                msg = "stat: File not found"
            return {"msg": msg}
