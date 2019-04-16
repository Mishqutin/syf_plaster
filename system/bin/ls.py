

class command:
    def main(path, args, cData):
        """List current directory elements."""
        if len(args)>0:
            return {"msg": ', '.join(os.listdir(args[0]))}
        else:
            return {"msg": ', '.join(os.listdir())}
