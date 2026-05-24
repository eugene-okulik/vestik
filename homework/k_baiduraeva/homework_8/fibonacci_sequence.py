import sys
sys.set_int_max_str_digits(100000)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def get_fib_num(n):
    count = 0
    for number in fibonacci():
        count += 1
        if count == n:
            return number


print(get_fib_num(5))
print(get_fib_num(200))
print(get_fib_num(1000))
print(get_fib_num(100000))
