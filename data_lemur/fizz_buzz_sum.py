def fizz_buzz_sum(target):
  ##get sum for 5 
  ## get sum for 3 
  op = list()
  sum_3 = 0
  sum_5 = 0 
  for i in range(2,target):
    if i % 3 == 0:
        
        sum_3 += i 
    elif i%5 == 0 :
        
        sum_5  += i 
      
  return sum_5 + sum_3

print(fizz_buzz_sum(16))
