

class command:
    def main(path, args, cData):
        """Print current working directory."""
        return {"msg": os.getcwd()}
