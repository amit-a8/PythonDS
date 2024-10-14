def max_subarray_sum(input):
  n = len(input)
  max_sum = 0 
  curr_sum = 0 
  for i in range(n):
    curr_sum += input[i]
    max_sum = max(curr_sum, max_sum)
    if curr_sum < 0:
      curr_sum = 0 
      
  return max_sum 
