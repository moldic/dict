
class Token:
    def value(self):
        return self.str

    def __init__(self,str):
        self.str=str


class Format:

    def __init__(self,str,dl):
        self.tokens=list(map(lambda x:Token(x),str.split(dl)))
