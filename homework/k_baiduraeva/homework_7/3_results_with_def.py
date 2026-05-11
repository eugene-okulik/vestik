line_1 = 'результат операции: 42'
line_2 = 'результат операции: 54'
line_3 = 'результат работы программы: 209'
line_4 = 'результат: 2'


def result(line):
    # number = int(line[line.index(':') + 1:])
    number = int(line.split(':')[1])
    print(number + 10)


result(line_1)
result(line_2)
result(line_3)
result(line_4)
