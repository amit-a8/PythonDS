def is_bad_version(num):
    if num == 67:
        return True
    return False


def first_bad_version(n):
  start = 1
  end = n
  num_of_call = 0
  
  while start <= end:
    mid = start + (end - start)//2
    api_resp = is_bad_version(mid)
    num_of_call += 1
    if api_resp:
      end = mid -1 
    else:
      start = mid + 1 
  return [start,num_of_call]


print(first_bad_version(100))
