import GlobalState as gs 
import os

class AliasAdd:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists(gs.ALIAS_FILE_PATH):
            with open(gs.ALIAS_FILE_PATH,"w") as _:
                pass

        print("Add A Program")
        cmd = input(" cmd: ").strip()
        alias = input(" alias: ").strip()
        if len(cmd) == 0 or len(alias) == 0:
            return


        with open(gs.ALIAS_FILE_PATH,"a") as f:
            f.write(cmd + ":" + alias + "\n")
    @staticmethod   
    def docs():
        return "adds a program into the runable programs list"    
    

