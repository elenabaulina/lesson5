poema = open("my_poema.txt", "w")
n = 1
while True:
    msg = "Введите " + str(n) + " строку поэмы: (для выхода нажмите два раза Enter)"
    s = input(msg)
    if s == '': break
    n+=1
    poema.write(s + '\n')
poema.close
f = open('stih.txt')
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()