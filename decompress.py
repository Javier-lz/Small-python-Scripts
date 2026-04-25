import os 
import shutil
from pathlib import Path 
import pathlib
import sys 


def main(): 
    decompress_direct:pathlib.Path = pathlib.Path(sys.argv[1])
    folder_path=pathlib.Path.cwd() / "All"
    folder =  pathlib.Path.mkdir(folder_path, exist_ok=True)
    if ( decompress_direct.exists()):
        
        for file in decompress_direct.rglob("*") : 
            print(file)
            print(file.is_file())
            if file.is_file() and folder_path not in file.parents:
                shutil.copy(str(pathlib.Path.cwd() / file),str(folder_path) )

    else: 
        raise "File does not exist"
        return 
    



main() 


