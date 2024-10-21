import GlobalState as gs 
import os

class RunList:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists(gs.PROGRAMS_FILE_PATH):
            with open(gs.PROGRAMS_FILE_PATH,"w") as _:
                pass

        prgs = []
        with open(gs.PROGRAMS_FILE_PATH,"r") as f:
            for line in f:
                if line:
                    program , path = line.split(":")
                    prgs.append((program,path))         

        if len(prgs) == 0: 
            print("You dont have any saved programs")
            return
        print("List Programs")
        for prg in prgs:
            print(" "+ prg[0])
    @staticmethod   
    def docs():
        return "lists all runable programs"    