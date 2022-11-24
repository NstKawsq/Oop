import testing_class_constr


class Cont:
    length = 100
    container = ['']*length

    def input(self, filename='in.txt'):
        flag = 0
        i = 0
        try:
            with open(filename, "r", encoding='utf-8') as fin:
                with open("out.txt", "w", encoding='utf-8') as fileout:
                    for line in fin.readlines():
                        if i == 100:
                            break
                        else:
                            part = line.split("|")
                            if len(part) == 4:
                                if (part[0] == '1') | (part[0] == '0') | (part[0] == '2'):
                                    if ((part[3] == '0\n') | (part[3] == '1\n') | (part[3] == '2\n') | (
                                            part[3] == '3\n') | (part[3] == '4\n') | (part[3] == '5\n') | (
                                            part[3] == '6\n') | (part[3] == '7\n') | (part[3] == '8\n') | (
                                            part[3] == '9\n') | (part[3] == '10\n')):
                                        if part[0] == '0':
                                            self.container[i] = testing_class_constr.Aforizm(part[0], part[2],
                                                                                             part[3], part[1])
                                            i += 1
                                        elif part[0] == '1':
                                            self.container[i] = testing_class_constr.Quot(part[0], part[2],
                                                                                          part[3], part[1])
                                            i += 1
                                        elif part[0] == '2':
                                            self.container[i] = testing_class_constr.Riddle(part[0], part[2],
                                                                                            part[3], part[1])
                                            i += 1
                                    else:
                                        flag = 1
                                        print('неверная субъективная оценка')
                                else:
                                    flag = 1
                                    print('неверная типизация')
                            else:
                                flag = 1
                                print('неверное количество ключевых моментов')
                        fileout.write('Контейнер заполнен')
        except FileNotFoundError:
            flag = 1
            print('такого файла не существует!')
        if i == 0:
            flag = 1
            print('файл пустой')
        return i, flag

    def out(self, filename='out.txt'):
        container_filled_sections = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open(filename, "a", encoding='utf-8') as fileout:
                    fileout.write(f'\nКонтейнер содержит {i} элементов:')
                    container_filled_sections = i
                break
        with open(filename, "a", encoding='utf-8') as fileout:
            if container_filled_sections != 0:
                for j in range(0, container_filled_sections):
                    self.container[j].printMe(fileout)
            elif container_filled_sections == 0:
                fileout.write(f'\nКонтейнер содержит {container_filled_sections} элементов:')
                fileout.write(f'\nКонтейнер очень пуст')

    def clear(self):
        self.container = []

    def mark_count(self, filename='out.txt'):
        container_filled_sections = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open(filename, "a", encoding='utf-8') as fileout:
                    fileout.write(f'\nКонтейнер содержит {i} элементов:')
                    container_filled_sections = i
                break
        mark_example = '",.;:!?)(/'

        with open(filename, "a", encoding='utf-8') as fileout:
            for i in range(0, container_filled_sections):
                punctuation_signs_count = 0
                for mark in mark_example:
                    temp_str = self.container[i].content
                    for j in range(len(temp_str)):
                        if temp_str[j].find(mark) != -1:
                            punctuation_signs_count += 1

                fileout.write(f'\nВ строке {i}, содержится {punctuation_signs_count} знаков препинания')
                return punctuation_signs_count

    def mark_for_sort(self, container):
        punctuation_signs_count = 0
        punctuation_mark = '"",.;:!?/'
        for mark in punctuation_mark:
            temp_str = container.content
            for j in range(len(temp_str)):
                if temp_str[j].find(mark) != -1:
                    punctuation_signs_count += 1
        return punctuation_signs_count

    def sort(self):
        container_filled_sections = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                container_filled_sections = i
                break
        for i in range(container_filled_sections - 1):
            for j in range(container_filled_sections - i - 1):
                if self.mark_for_sort(self.container[j]) < self.mark_for_sort(self.container[j+1]):
                    self.container[j], self.container[j+1] = self.container[j+1], self.container[j]

    def filtered_output_by_quotation(self, filename='out.txt'):
        container_filled_sections = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open(filename, "a", encoding='utf-8') as fileout:
                    fileout.write(f'\nКонтейнер содержит {i} элементов:')
                    container_filled_sections = i
                break

        with open(filename, "a", encoding='utf-8') as fileout:
            if container_filled_sections != 0:
                for j in range(0, container_filled_sections):
                    if self.container[j].index == '0':
                        self.container[j].printMe(fileout)

    def filtered_output_by_aforizm(self, filename='out.txt'):
        container_filled_sections = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                with open(filename, "a", encoding='utf-8') as fileout:
                    fileout.write(f'\nКонтейнер содержит {i} элементов:')
                    container_filled_sections = i
                break

        with open(filename, "a", encoding='utf-8') as fileout:
            if container_filled_sections != 0:
                for j in range(0, container_filled_sections):
                    if self.container[j].index == '1':
                        self.container[j].printMe(fileout)

    def multi(self):
        razmernost = 0
        for i in range(len(self.container)):
            if self.container[i] == "":
                razmernost = i
                break

        i = 0
        multi_string = [''] * 3
        if razmernost != 0:
            for j in range(0, razmernost):
                if self.container[j].index == '0':
                    multi_string[i % 3] = 'Цитата'
                elif self.container[j].index == '1':
                    multi_string[i % 3] = 'Афоризм'
                elif self.container[j].index == '2':
                    multi_string[i % 3] = 'Загадка'
                i += 1
                razmernost -= 1

                if i == 3:
                    print(f'{multi_string[0]} и {multi_string[1]} и {multi_string[2]}')
                    i = 0
                    multi_string = [''] * 3
                elif razmernost == 0:
                    if i==1:
                        print(f'{multi_string[0]}')
                    elif i==2:
                        print(f'{multi_string[0]} и {multi_string[1]}')
