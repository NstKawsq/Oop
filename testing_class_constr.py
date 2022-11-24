class Mudrost():
    def __init__(self, index, content,mark):
        self.index=index
        self.content=content
        self.mark=mark

    def printMe(self, fout):
        fout.write(f'\nЭто мудрость {self.content}')

class Quot(Mudrost):
    def __init__(self, index, content, mark, name):
        Mudrost.__init__(self, index, content,mark)
        self.name=name
    def printMe(self, fout):
        fout.write(f'\nЭто цитата {self.name} : {self.content}')


class Aforizm(Mudrost):
    def __init__(self, index, content,mark, country):
        Mudrost.__init__(self, index, content,mark)
        self.country = country
    def printMe(self, fout):
        fout.write(f'\nЭто афоризм {self.country} : {self.content} ')


class Riddle(Mudrost):
    def __init__(self, index, content, answer):
        Mudrost.__init__(self, index, content)
        self.answer = answer
    def printMe(self, fout):
        fout.write(f'\nЭто загадка : {self.content} - {self.answer} ')
