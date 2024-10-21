class Renderer:
    text_style_map = {
        "bold" : "ESC[22m",
        "light" : "ESC[22m	",
        "italic" : "ESC[23m",
    }

    @staticmethod
    def print(text,style = ""):
        print(style,end="")
        print(text)


renderer =  Renderer
renderer.print("UR MOM","\x1b[1")