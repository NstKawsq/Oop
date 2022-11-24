import class_construct
def qout_in(container,i,part):
    container[i] = class_construct.Quotation()
    container[i].index = part[0]
    container[i].name = part[1]
    container[i].content = part[2]