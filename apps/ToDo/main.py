import rich


print("TODO: ")
while True:
    print(">> ",end="")
    cmd = input().strip()
    args = ""
    if len(cmd.split(" ")) != 1:
        cmd , args = cmd.split(" ")

    if cmd == "add":
        todo = input(" Add >> ")
    elif cmd == "list":
        pass
    elif cmd == "tags":
        pass
    elif cmd == "exit":
        break