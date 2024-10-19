import GlobalState as gs 
import os

class AliasRemove:
    @staticmethod   
    def exec(args : list = []):
        alias = args[0]

        if not os.path.exists(gs.ALIAS_FILE_PATH):
            with open(gs.ALIAS_FILE_PATH,"w") as _:
                pass

        lines = ""
        found = False
        with open(gs.ALIAS_FILE_PATH,"r") as f:
            line  = f.readline()
            if not line.find(alias):
                found = True
                lines += line + "\n"
        lines.strip()
        with open(gs.ALIAS_FILE_PATH,"w") as f:
            f.write(lines)

        if not found:
            print(f"Failed to find the alias '{alias}'")

    @staticmethod   
    def docs():
        return "removes a alias, remove <alias>"    