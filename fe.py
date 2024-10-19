import cmds.GlobalState as  gs
from cmds.Help import Help
from cmds.Run.Run import Run

class FE:
    @staticmethod
    def exec(cmd):
        FE.init()
        path = cmd.pop(0)

        if len(cmd) == 0 or  cmd[0] not in gs.CMDS:
            print("unknown cmd was provided")
            gs.exec(gs.Cmds.help)
            return
        
        gs.exec(cmd.pop(0),cmd)


    @staticmethod 
    def init():
        Run.init()
        gs.CMDS = {
            gs.Cmds.help._name_ : Help,
            gs.Cmds.run._name_ : Run,
        }
