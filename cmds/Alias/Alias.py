import GlobalState as gs 
from cmds.Alias.Help import AliasHelp  
from cmds.Alias.List import AliasList  
from cmds.Alias.Add import AliasAdd  
from cmds.Alias.Remove import AliasRemove  

import os

class Alias:
    @staticmethod   
    def exec(args : list = []):
        if len(args) == 0 or args[0] not in gs.ALIAS_CMDS.keys():
            if len(args) == 0:
                print(f"expected args and got nothing")
            else:
                print(f"unknown cmd was provided '{args[0]}'")
                gs.exec(gs.AliasCmds.help,[],gs.ALIAS_CMDS)
            return
        
        gs.exec(args.pop(0),args,gs.ALIAS_CMDS)


    @staticmethod   
    def docs():
        return "excutes a pre-defined alias"    
    
    @staticmethod
    def init():
        gs.ALIAS_CMDS = {
            gs.AliasCmds.help._name_ : AliasHelp,
            gs.AliasCmds.list._name_ : AliasList,
            gs.AliasCmds.add._name_ :  AliasAdd,
            gs.AliasCmds.remove._name_ :  AliasRemove,
        }

    @staticmethod 
    def check_alias(searched) -> tuple[str,bool]:
        if not os.path.exists(gs.ALIAS_FILE_PATH): return (False,"")

        aliases = []    
        with open(gs.ALIAS_FILE_PATH,"r") as f:
            for line in f:
                if line:
                    cmd , alias = line.split(":")
                    aliases.append((cmd.strip(),alias.strip()))
                    if aliases[-1][1] == searched:
                        return (True,cmd)
        return (False,"")