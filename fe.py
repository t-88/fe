import GlobalState as  gs
from cmds.Help import Help
from cmds.Run.Run import Run
from cmds.Alias.Alias import Alias
import os

class FE:
    @staticmethod
    def exec(cmd):
        path = cmd.pop(0)

        if len(cmd) == 0:
            print(f"expected args and got nothing")
            gs.exec(gs.Cmds.help)
            return
        elif cmd[0] not in gs.CMDS:
            (is_alias, prg) = Alias.check_alias(cmd[0]) 
            if is_alias:
                os.system(prg + " " +"".join(cmd[1:]))
                return             

            print(f"unknown cmd was provided '{cmd[0]}'")
            gs.exec(gs.Cmds.help)

        gs.exec(cmd.pop(0),cmd)

    @staticmethod 
    def init():
        gs.init()
        Run.init()
        Alias.init()
        gs.CMDS = {
            gs.Cmds.help._name_ : Help,
            gs.Cmds.run._name_ : Run,
            gs.Cmds.alias._name_ : Alias,
        }
