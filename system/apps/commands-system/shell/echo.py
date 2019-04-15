

class command:
    def main(path, args, cData):
        """Usage: echo <message>
        Echo message back to client."""
        return {"msg": ' '.join(args)}
