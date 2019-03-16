import os
import sys
import zipfile





def ziprun(filepath, runArgs={}):
    abspath  = os.path.abspath(filepath)
    
    basepath = os.path.dirname(abspath)
    filename = os.path.basename(abspath)
    
    
    zip = zipfile.ZipFile(filepath, 'r')
    
    
    code = zip.read("_ziprun.py")
    
    execLocals = {
                 'abspath': abspath,
                 'basepath': basepath,
                 'filename': filename,
                 'zip': zip,
                 **runArgs
                 }
    
    exec(code, {}, execLocals)
    

if __name__=="__main__":
    if len(sys.argv)==2:
        path = sys.argv[1]
        args = {}
        ziprun(path, args)
    elif len(sys.argv)==3:
        path = sys.argv[1]
        args = eval(sys.argv[2])
        ziprun(path, args)
    else:
        print("Not enough or too many arguments.")
        print("ziprun <path> [dict-like string with arguments]")
        
    
    
    


