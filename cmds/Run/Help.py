import cmds.GlobalState as gs 


class RunHelp:
    @staticmethod   
    def exec(args : list = []):
        print("run help:")
        print("\tsyntax: run <program name>")
        print("\tcmds:")
        for cmd in gs.RUN_CMDS.keys():
            print("\t\t",end="")
            print(cmd.lower() + ":",gs.RUN_CMDS[cmd].docs())
            
    @staticmethod   
    def docs():
        return "show run help"    