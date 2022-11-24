import input_shape

def container_filling(container):
    i=0
    with open("in.txt", "r", encoding='utf-8') as fin:
        with open("out.txt", "w", encoding='utf-8') as fout:
            for line in fin.readlines():
                part=line.split("|")

                input_shape.fill_container(container,i,part)
                i=i+1

            fout.write('Контейнер заполнен')