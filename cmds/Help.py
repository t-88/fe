from cmds.GlobalState import *
import cmds.GlobalState as gs 

class Help:
    @staticmethod   
    def exec(args : list = []):
        print("help:")
        for cmd in gs.CMDS.keys():
            print("\t",end="")
            print(cmd.lower() + ":",gs.CMDS[cmd].docs())
    
    @staticmethod   
    def docs():
        return "show help"
