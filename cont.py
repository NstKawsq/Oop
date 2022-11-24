import testing_class_constr

class cont():
    length=100
    container=['']*length

    def input(self):
        i=0
        with open("in.txt", "r", encoding='utf-8') as fin:
            with open("out.txt", "w", encoding='utf-8') as fout:
                for line in fin.readlines():
                    part = line.split("|")
                    if part[0] == '0':
                        self.container[i] = testing_class_constr.Aforizm(part[0], part[2], part[3], part[1])

                        print(self.container[i].country)
                        i += 1

                    elif part[0] == '1':

                        self.container[i] = testing_class_constr.Quot(part[0], part[2], part[3], part[1])

                        print(self.container[i].name)
                        i += 1

                    elif part[0] == '2':

                        self.container[i] = testing_class_constr.Riddle(part[0], part[2], part[3], part[1])

                        print(self.container[i].answer)
                        i += 1

                fout.write('Контейнер заполнен')


    def out(self):
        type = ''
        razmernost = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open("out.txt", "a", encoding='utf-8') as fout:
                    fout.write(f'\nКонтейнер содержит {i} элементов:')
                    razmernost = i
                break

        with open("out.txt", "a", encoding='utf-8') as fout:
            if razmernost != 0:
                for j in range(0, razmernost):

                    # shape in
                    # type=shape_in.determine_shape(container,j)
                    self.container[j].printMe(fout)

            elif razmernost == 0:
                fout.write(f'\nКонтейнер содержит {razmernost} элементов:')
                fout.write(f'\nКонтейнер очень пуст')

    def clear(self):
        self.container=[]

    def mark_count(self):
        razmernost = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open("out.txt", "a", encoding='utf-8') as fout:
                    fout.write(f'\nКонтейнер содержит {i} элементов:')
                    razmernost = i
                break
        mark_example = '",.;:!?)(\/'

        with open("out.txt", "a", encoding='utf-8') as fout:
            for i in range(0, razmernost):
                punc_count = 0
                for mark in mark_example:
                    str = self.container[i].content
                    for j in range(len(str)):
                        if str[j].find(mark) != -1:
                            punc_count += 1

                fout.write(f'\nВ строке {i}, содержится {punc_count} знаков препинания')

    def mark_for_sort(self, container):
        punc_count = 0
        punc_marks = '"",.;:!?\/'
        for mark in punc_marks:
            str = container.content
            for j in range(len(str)):
                if str[j].find(mark) != -1:
                    punc_count += 1
        return punc_count

    def sort(self):
        for i in range(len(self.container)):
            if self.container[i] == "":
                razmernost = i
                break

        for i in range(razmernost - 1):
            for j in range(razmernost - i - 1):
                if self.mark_for_sort(self.container[j]) < self.mark_for_sort(self.container[j+1]):
                    self.container[j], self.container[j+1] = self.container[j+1], self.container[j]

    def filtered_output_by_quotation(self):
        razmernost = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open("out.txt", "a", encoding='utf-8') as fout:
                    fout.write(f'\nКонтейнер содержит {i} элементов:')
                    razmernost = i
                break

        with open("out.txt", "a", encoding='utf-8') as fout:
            if razmernost != 0:
                for j in range(0, razmernost):
                    if self.container[j].index == '0':
                        self.container[j].printMe(fout)

    def filtered_output_by_aforizm(self):
        razmernost = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open("out.txt", "a", encoding='utf-8') as fout:
                    fout.write(f'\nКонтейнер содержит {i} элементов:')
                    razmernost = i
                break

        with open("out.txt", "a", encoding='utf-8') as fout:
            if razmernost != 0:
                for j in range(0, razmernost):

                    # shape in
                    # type=shape_in.determine_shape(container,j)
                    if self.container[j].index == '1':
                        self.container[j].printMe(fout)

