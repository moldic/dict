
class Token:
    def value(self):
        return self.str

    def __init__(self,str):
        self.str=str
        self.tokens=[]

    def add(self,Token):
        self.tokens.add(Token)

    #dummy
    def next(self):
        return ''

class InputText:
    def __init__(self,str,dl):
        self.tokens=list(map(lambda x:Token(x),str.split(dl)))

#Cannot-Recursive
#str:row-string
class Format:
    def lex(self,str,tokens=[]):
        while len(str)!=0:
            if (i:=str.find('{'))!=-1:
                tokens.append(str[:i])
                str=str[i+1:]
                print(str)
                break
            else:
                tokens.append(str)
                break
        return tokens

    def __init__(self,str):
        #validator
        if str.count('{')!= str.count('}'):
            return
        #token
        self.lex(str)


Format('hoge{h}oge')