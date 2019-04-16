

class command:
    def main(path, args, cData):
        """Usage: cd <path>
        Change directory."""
        try:
            os.chdir(args[0])
        except Exception as e:
            return {"msg": str(e)}
