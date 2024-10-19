import GlobalState as gs 
from cmds.Run.Help import RunHelp  
from cmds.Run.List import RunList  
from cmds.Run.Add import RunAdd  



class Run:
    @staticmethod   
    def exec(args : list = []):
        if len(args) == 0 or args[0] not in gs.RUN_CMDS.keys():
            if len(args) == 0:
                print(f"expected args and got nothing'")
            else:
                print(f"unknown cmd was provided '{args[0]}'")

                gs.exec(gs.RunCmds.help,[],gs.RUN_CMDS)
            return
        gs.exec(args.pop(0),args,gs.RUN_CMDS)


    @staticmethod   
    def docs():
        return "runs a pre-defined cmd"    
    
    @staticmethod
    def init():
        gs.RUN_CMDS = {
            gs.RunCmds.help._name_ : RunHelp,
            gs.RunCmds.list._name_ : RunList,
            gs.RunCmds.add._name_ :  RunAdd,
        }
