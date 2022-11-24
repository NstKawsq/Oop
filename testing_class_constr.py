class Mudrost():
    def __init__(self, index, content,mark):
        self.index=index
        self.content=content
        self.mark=mark

class Quot(Mudrost):
    def __init__(self, index, content, mark, name):
        Mudrost.__init__(self, index, content,mark)
        self.name=name


class Aforizm(Mudrost):
    def __init__(self, index, content,mark, country):
        Mudrost.__init__(self, index, content,mark)
        self.country = country
