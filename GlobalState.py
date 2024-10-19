from enum import Enum
import os

Cmds = Enum("Cmds",["help","run","alias"])
CMDS = {}

RunCmds = Enum("Cmds",["help","add","list"])
RUN_CMDS = {}

AliasCmds = Enum("Cmds",["help","add","list","remove"])
ALIAS_CMDS = {}

DB_PATH =f"{os.path.expanduser('~')}/.config/fe"
PROGRAMS_FILE_PATH = f"{DB_PATH}/programs"
ALIAS_FILE_PATH = f"{DB_PATH}/aliases"


def init():
    os.makedirs(DB_PATH,exist_ok=True)

def exec(cmd : Cmds | str,args : list = [], cmdMap : dict = {}):
    cmdMap = CMDS if len(cmdMap.keys()) == 0  else cmdMap

    if type(cmd) != str: 
        cmd = cmd._name_
    
    cmdMap[cmd].exec(args)