import heapq

def max_three(input):
  top_list = list()
  for each_elt in input:
    heapq.heappush(top_list,-1* each_elt)
  prod = 1
  for i in range(3):
    prod = prod * (-1 * heapq.heappop(top_list))
  
  return prod

max_three([1, 3, 4, 5])
