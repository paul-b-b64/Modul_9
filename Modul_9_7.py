def is_prime(funk):
    def wrapper(*numbers):
        num = funk(*numbers)
        if num < 2:
            return 'Число меньше двух'
        if num == 2:
            return f'Простое\n{num}'
        for i in range(2, num):
            if num % i == 0:
                return f'Составное\n{num}'
            return f'Простое\n{num}'

    return wrapper


@is_prime
def sum_three(a, b, c):
    sum3 = a + b + c
    return sum3


result = sum_three(2, 3, 6)
print(result)
