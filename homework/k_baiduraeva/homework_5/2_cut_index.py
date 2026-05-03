line_1 = ('результат операции: 42')
line_2 = ('результат операции: 514')
line_3 = ('результат работы программы: 9')

index_operation = line_1.index(':')
index_program = line_3.index(':')

print(int(line_1[index_operation + 1:]) + 10)
print(int(line_2[index_operation + 1:]) + 10)
print(int(line_3[index_program + 1:]) + 10)
