def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum


def is_happy_number(n):
    print(sum_of_squared_digits(n))
    fast_ptr = sum_of_squared_digits(n)
    slow_ptr = n 
    while fast_ptr != 1 and fast_ptr != slow_ptr:
        slow_ptr = sum_of_squared_digits(slow_ptr)
        fast_ptr = sum_of_squared_digits(sum_of_squared_digits(fast_ptr))
    
    
    if fast_ptr == 1:
        return True 
    return False


print(is_happy_number(2147483646))


def hello_world():
    print("aa")
