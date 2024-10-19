import cmds.GlobalState as gs 
import os

class RunList:
    @staticmethod   
    def exec(args : list = []):
        if not os.path.exists("programs"):
            with open("programs","w") as _:
                pass

        prgs = []
        with open("programs","r") as f:
            line  = f.readline()
            if line:
                program , path = line.split(":")
                prgs.append((program,path))

        if len(prgs) == 0: 
            print("You dont have any saved programs")
            return
        print("List programs")
        for prg in prgs:
            print(" "+ prg[0])
    @staticmethod   
    def docs():
        return "lists all runable programs"    