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
            for line in f:
                if line.split(":")[1].strip() != alias:
                    lines += line 
                else:
                    found = True

        lines = lines.strip()
        with open(gs.ALIAS_FILE_PATH,"w") as f:
            f.write(lines)

        if not found:
            print(f"Failed to find the alias '{alias}'")

    @staticmethod   
    def docs():
        return "removes a alias, remove <alias>"    