def out_aforizm(container,j,type):
    with open("out.txt", "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].country} - {container[j].content}')