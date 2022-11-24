import output_shape
def print_container(container):

    razmernost = 0
    for i in range(len(container)):
        if container[i] == "":
            with open("out.txt", "a", encoding='utf-8') as fout:
                fout.write(f'\nКонтейнер содержит {i} элементов:')
                razmernost = i
            break

    with open("out.txt", "a", encoding='utf-8') as fout:
        if razmernost != 0:
            for j in range(0, razmernost):
                output_shape.out_shape(container,j)

        elif razmernost == 0:
            fout.write(f'\nКонтейнер содержит {razmernost} элементов:')
            fout.write(f'\nКонтейнер очень пуст')