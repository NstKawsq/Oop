def out_quot(container,j,type):
    with open("out.txt", "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].name} - {container[j].content}')