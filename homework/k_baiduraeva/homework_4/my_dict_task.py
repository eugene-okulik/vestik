my_dict = {
    'tuple': (7.2, 'Hello', 13, True, 'hello'),
    'list': ['first', 2, 'Third', 4.1, '5'],
    'dict': {
        '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'
    },
    'set': {1, 3, 5, 7, 21}
}

print(my_dict)

print(my_dict['tuple'][-1])

my_dict['list'].append('new')
my_dict['list'].pop(1)

# my_dict['dict']['i am a tuple'] = 17
print(type(my_dict['dict']))
my_dict['dict'][('i am a tuple',)] = 17
my_dict['dict'].pop('1')

my_dict['set'].add(19)
my_dict['set'].remove(3)

print(my_dict)
