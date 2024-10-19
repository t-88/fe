import GlobalState as gs 
import os

class RunAdd:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists(gs.PROGRAMS_FILE_PATH):
            with open(gs.PROGRAMS_FILE_PATH,"w") as _:
                pass

        print("Add A Program")
        name = input(" name: ")
        path = input(" path: ")

        with open(gs.PROGRAMS_FILE_PATH,"a") as f:
            f.write(name + ":" + path + "\n")
    @staticmethod   
    def docs():
        return "adds a program into the runable programs list"    
    

