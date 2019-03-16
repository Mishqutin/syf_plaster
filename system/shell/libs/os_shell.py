import subprocess



def RunShell(args, errContinue=False):
    if errContinue:
        try:
            return subprocess.run(args, shell=False, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")
        except Exception as e:
            print(e)
            print("\n====Process will continue.====")
            return e
    else:
        return subprocess.run(args, shell=False, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")