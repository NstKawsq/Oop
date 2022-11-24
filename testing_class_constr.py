class Mudrost():
    def __init__(self, index, content,mark):
        self.index=index
        self.content=content
        self.mark=mark

    def printMe(self, fout):
        fout.write(f'\nЭто мудрость {self.content} и ее оценка {self.mark}')

class Quot(Mudrost):
    def __init__(self, index, content, mark, name):
        Mudrost.__init__(self, index, content,mark)
        self.name=name
    def printMe(self, fout):
        fout.write(f'\nЭто цитата {self.name} : {self.content} и ее оценка {self.mark}')


class Aforizm(Mudrost):
    def __init__(self, index, content,mark, country):
        Mudrost.__init__(self, index, content,mark)
        self.country = country
    def printMe(self, fout):
        fout.write(f'\nЭто афоризм {self.country} : {self.content} и ее оценка {self.mark}')


class Riddle(Mudrost):
    def __init__(self, index, content,mark, answer):
        Mudrost.__init__(self, index, content, mark)
        self.answer = answer
    def printMe(self, fout):
        fout.write(f'\nЭто загадка : {self.content} - {self.answer} и ее оценка {self.mark}')
