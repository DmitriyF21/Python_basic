"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    prime_numbers = []
    for n in range(num):
        if num > 1:
            is_prime = True
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers





def filter_numbers(list_number, type_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    def fltr_func(num):
        if type_filter == ODD:
            if num % 2!=0:
                return True
            else:
                return False
        if type_filter == EVEN:
            if num % 2==0:
                return True
            else:
                return False
        if type_filter == PRIME:
            return is_prime(num)
    return list(filter(fltr_func, list_number))
nums=[0,1,2,3,4,5,11,121]
c=filter_numbers(nums, PRIME)
print(c)








