class Mudrost():
    def __init__(self, index, content):
        self.index=index
        self.content=content

class Quot(Mudrost):
    def __init__(self, index, content, name):
        Mudrost.__init__(self, index, content)
        self.name=name


class Aforizm(Mudrost):
    def __init__(self, index, content, country):
        Mudrost.__init__(self, index, content)
        self.country = country


class riddle(Mudrost):
    def __init__(self, index, content, answer):
        Mudrost.__init__(self, index, content)
        self.answer=answer