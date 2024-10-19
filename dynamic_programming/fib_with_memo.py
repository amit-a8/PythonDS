fib_memo = dict()
fib_memo[0] = 0
fib_memo[1] =1 
fib_memo[2] = 2 
def find_tribonacci(n):

    # Replace this placeholder return statement with your code
  if n <=0:
    return 0 
  elif n <3:
    return 1
  else:
    if n not  in fib_memo.keys():
      fib_memo[n] =  find_tribonacci(n-3) + find_tribonacci(n-1) + find_tribonacci(n-2)
    return fib_memo[n]
