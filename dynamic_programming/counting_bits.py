def counting_bits(n):
    output_arr = list()
    output_arr.append(0)
    for each_num in range(1,n+1):
      this_binary_string = bin(each_num).count("1")
      output_arr.append(this_binary_string)
    # Replace this placeholder return statement with your code
    return output_arr
