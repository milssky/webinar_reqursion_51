# сумма числе в списке

def recursion_sum_nums_in_list(nums: list[int]) -> int:
    if not nums:
        return 0
    return recursion_sum_nums_in_list(nums[1:]) + nums[0]


# print(recursion_sum_nums_in_list([1, 2, 3, 4, 5]))


# сумма чисел в списке с поддержкой вложенных списков
# [1,2,3, [4,5 [6,7]]] = 28

def recursion_sum_num_of_list_in_list(nums:list) -> int:
    summ = 0
    for element in nums:
        if not type(element) == list:
            summ += element
        else:
            summ += recursion_sum_num_of_list_in_list(element)
    return summ


# print(recursion_sum_num_of_list_in_list([1, 2, 3, [4, 5, [6, 7]]]))


def count_negative_nums_in_list(nums: list) -> int:
    if not nums:  # []
        return 0
    count = count_negative_nums_in_list(nums[1:])
    if nums[0] < 0:
        count += 1
    return count


# print(count_negative_nums_in_list([-1, -2, 1, 1, 1, -2, 1]))


# Реверсирование числа. 123 -> 321 = 3*10^2 + 2*10^1 + 1*10^0

def recursion_num_reverse(num):
    if num < 0:
        return -1
    if num == 0:
        return 0

    power = 0
    num_copy = num
    while num_copy > 0:
        power += 1
        num_copy //= 10

    last_digit = num % 10

    result = last_digit * 10**(power - 1)

    return result + recursion_num_reverse(num//10)


# print(recursion_num_reverse(12356789))

# Возвести число x в степень y

def recursion_power(x: int, y: int) -> int:
    if y == 0:
        return 1
    return x * recursion_power(x, y-1)


# print(recursion_power(2, 10))


# Определение максимального числа в списке

def recursion_max_in_list(nums: list) -> int:
    if len(nums) > 1:
        max_num = recursion_max_in_list(nums[1:])
        if nums[0] < max_num:
            return max_num
    return nums[0]


# print(recursion_max_in_list([9, 1, 1, 2, 3, 4, 5]))
# print(recursion_max_in_list([0, 1, 1, 9, 3, 4, 5]))
# print(recursion_max_in_list([0, 1, 1, 2, 3, 4, 9]))


# Перевод из 10 системы счисления в двоичную

def dec_2_bin(n: int) -> int:
    power = 0
    result = 0
    while n > 0:
        ost = n % 2
        n = n // 2
        result += ost * 10**power
        power += 1
    return result


# print(dec_2_bin(37))


def recursion_dec_2_bin(n: int, power: int = 0) -> int:
    if n <= 0:
        return 0
    ost = n % 2
    return recursion_dec_2_bin(n//2, power+1) + ost*10**power


print(recursion_dec_2_bin(5))
