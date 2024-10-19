from enum import Enum

Cmds = Enum("Cmds",["help","run"])
CMDS = {}

RunCmds = Enum("Cmds",["help","add","list"])
RUN_CMDS = {}



def exec(cmd : Cmds | str,args : list = [], cmdMap : dict = {}):
    cmdMap = CMDS if len(cmdMap.keys()) == 0  else cmdMap

    if type(cmd) != str: 
        cmd = cmd._name_
    
    cmdMap[cmd].exec(args)