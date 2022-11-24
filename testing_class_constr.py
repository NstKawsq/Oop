class Mudrost():
    def __init__(self, index, content):
        self.index=index
        self.content=content

    def printMe(self, fout):
        fout.write(f'\n Mudr')

class Quot(Mudrost):
    def __init__(self, index, content, name):
        Mudrost.__init__(self, index, content)
        self.name=name
    def printMe(self, fout):
        fout.write(f'\n Quot')


class Aforizm(Mudrost):
    def __init__(self, index, content, country):
        Mudrost.__init__(self, index, content)
        self.country = country
    def printMe(self, fout):
        fout.write(f'\n Afor')
