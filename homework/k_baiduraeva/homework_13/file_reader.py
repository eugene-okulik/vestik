import os
import datetime


base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(hw_13_file_path)


def read_file():
    with open(hw_13_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for line in read_file():
    print(line.rstrip())


for line in read_file():
    number = line.split()[0]
    date_text = line.split()[1] + ' ' + line.split()[2]

    date = datetime.datetime.strptime(
        date_text,
        '%Y-%m-%d %H:%M:%S.%f'
    )

    if number == '1.':
        new_date = date + datetime.timedelta(days=7)
        print(new_date)

    elif number == '2.':
        print(date.strftime('%A'))

    elif number == '3.':
        difference = datetime.datetime.now() - date
        print(difference.days)
