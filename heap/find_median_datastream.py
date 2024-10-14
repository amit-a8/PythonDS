
from heapq import *
# Tip: You may use some of the code templates provided
# in the support files

class MedianOfStream:
  def __init__(self):
    # Write your code here
    self.min_heap_list = []
    self.max_heap_list = []

  # This function should take a number and store it
  def insert_num(self, num):
    if len(self.max_heap_list) == 0:
      heappush(self.max_heap_list, -1*  num)
    elif len(self.max_heap_list) > len(self.min_heap_list):
        if num > -1 * self.max_heap_list[0]:
            heappush(self.min_heap_list,  num)

        elif num < -1 * self.max_heap_list[0]:

            pop_elt = heappop(self.max_heap_list)

            heappush(self.min_heap_list, -1 * pop_elt)
            heappush(self.max_heap_list, -1 * num)

    elif len(self.min_heap_list) > len(self.max_heap_list):

        if num <  self.min_heap_list[0]:
            heappush(self.max_heap_list, -1* num)
        else:
            pop_elt = heappop(self.min_heap_list)
            heappush(self.max_heap_list, -1 * pop_elt)
            heappush(self.min_heap_list,  num)
    else:
        if num > -1 * self.max_heap_list[0]:
            heappush(self.min_heap_list,  num)
        else:
            heappush(self.max_heap_list, -1* num)

    

  # This function should return the median of the stored numbers
  def find_median(self):
    # Replace this placeholder return statement with your code

    median= None
    if len(self.max_heap_list) == len(self.min_heap_list):
      median =  (self.max_heap_list[0] * -1 + self.min_heap_list[0] )/2.0
    else:
      if len(self.max_heap_list) >  len(self.min_heap_list):
        median = self.max_heap_list[0] * -1 / 1.0
      elif len(self.max_heap_list) <  len(self.min_heap_list):
        median = self.min_heap_list[0] / 1.0 
    print(median)
    return median
