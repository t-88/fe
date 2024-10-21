import GlobalState as gs 
import os

class AliasList:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists(gs.ALIAS_FILE_PATH):
            with open(gs.ALIAS_FILE_PATH,"w") as _:
                pass

        aliases = []
        with open(gs.ALIAS_FILE_PATH,"r") as f:
            for line in f:
                if line:
                    cmd , alias = line.split(":")
                    aliases.append((cmd.strip(),alias.strip()))


        if len(aliases) == 0: 
            print("You dont have any saved aliases")
            return
        print("List Aliases")
        for prg in aliases:
            print(" "+ prg[1] + " : " + prg[0] )
    @staticmethod   
    def docs():
        return "lists all aliases"    