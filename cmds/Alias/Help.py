import GlobalState as gs 


class AliasHelp:
    @staticmethod   
    def exec(args : list = []):
        print("alias help:")
        print("\tsyntax: fe <alias>")
        print("\tcmds:")
        for cmd in gs.ALIAS_CMDS.keys():
            print("\t\t",end="")
            print(cmd.lower() + ":",gs.ALIAS_CMDS[cmd].docs())
            
    @staticmethod   
    def docs():
        return "show alias help"    