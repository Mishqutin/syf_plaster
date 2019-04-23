# Run files multi-platform.
import subprocess


def runFile(param):
    """param - can bes string or list."""

    res = subprocess.run(param, shell=False, check=True, stdout=subprocess.PIPE).stdout.decode("UTF-8")

    return res

