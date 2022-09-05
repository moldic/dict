
class Token:
    def getValue(self):
        return self.str

    def __init__(self,str):
        self.str=str
        self.tokens=[]

    def add(self,Token):
        self.tokens.append(Token)

    #dummy
    def next(self):
        return ''

class Fr(Token):
    def __init__(self):
        self.str=('{')


class To(Token):
    def __init__(self):
        self.str=('}')

class InputText:
    def __init__(self,str,dl):
        self.tokens=list(map(lambda x:Token(x),str.split(dl)))

#str:row-string
class Format:
    #split into Token
    def lex(self,str):
        delimiters={'{':Fr,'}':To}
        for i in range(len(str)):
            if (c:=str[i]) in delimiters:
                if i!=0:
                    self.tokens.append(str[0:i])
                self.tokens.append(delimiters.get(c)())
                self.lex(str[i+1:])
                break
            if i==len(str)-1:
                self.tokens.append(str)        

    def __init__(self,str): 
        self.tokens=[]
        #validator
        if str.count('{')!= str.count('}'):
            return
        self.lex(str)


if __name__=='__main__':

    for i in Format('hoge{ho}ge').tokens:
        print(i)