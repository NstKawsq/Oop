def multik(container):
    razmernost = 0
    for i in range(len(container)):
        if container[i] == "":
            razmernost = i
            break

    multi_str=['']*2
    i=0
    with open("in.txt", "r", encoding='utf-8') as fin:
        for line in fin.readlines():
            part=line.split("|")
            if part[0]=='0':
                multi_str[i % 2]='Цитата'
            elif part[0]=='1':
                multi_str[i % 2]='Афоризм'
            i += 1
            razmernost -= 1

            if i == 2:
                print(f'{multi_str[0]} и {multi_str[1]}')
                multi_str = [''] * 2
                i = 0
            elif (razmernost == 0):
                print(f'{multi_str[0]}')
