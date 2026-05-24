import random

salary = int(input('Type your salary: '))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(100, 5000)
    salary += bonus_amount

print(f'${salary}')
