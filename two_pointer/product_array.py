def product_list(arr):
    product = 1
    i = 0
    j = len(arr)-1
    while i < j :
        product *= arr[i]*arr[j]
        i+= 1
        j-= 1

    if i ==j :
        product *= arr[i]
    return product


def product_except_self(nums):
    
    op = list()
    start = 0
    last = len(nums) -1
    
    for i, num in enumerate(nums):
        this_arr = nums[:i] + nums[i+1:]
        this_product = product_list(this_arr)
        op.append(this_product)
    return op 

    
input_arr = [0, -1, 2, -3, 4, -2]
#print(product_list(input_arr))
print(product_except_self(input_arr))
