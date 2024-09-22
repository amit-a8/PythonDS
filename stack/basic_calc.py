def basic_calculator(s):
    print(s)
    stack = list()
    numbers = list()
    sign = ['+', '-']
    parathesis = ['(', ')']
    split_val = s.split()
    print(split_val)
    for each_char in split_val:
                
        if each_char in sign:
            pass
        elif each_char in parathesis:
            pass
        if each_char.isdigit():
            numbers.append(each_char)
    print(numbers)


basic_calculator("(8 + 100) + (13 - 8 - (2 + 1))")
        
