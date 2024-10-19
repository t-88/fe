import cmds.GlobalState as gs 
import os

class RunAdd:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists("programs"):
            with open("programs","w") as _:
                pass

        print("Add program")
        name = input(" name: ")
        path = input(" path: ")

        with open("programs","a") as f:
            f.write(name + ":" + path)
    @staticmethod   
    def docs():
        return "adds a program into the runable programs list"    
    

