def merge_intervals(intervals):
    print(intervals)
    op_list = list()
    op_list.append(intervals[0])
    for each_interval in intervals[1:]:
      last_interval = op_list[-1]
      if each_interval[0] > last_interval[1]:
          op_list.append(each_interval)
      else:
          end = max(last_interval[1],each_interval[1])
          new_interval = [last_interval[0], end ]
          op_list.pop()
          op_list.append(new_interval)
    return op_list


def hello_world():
    print("hel")

def insert_interval(existing_intervals, new_interval):

  op_list = list()
  for i,each_interval in enumerate(existing_intervals):
    this_start = each_interval[0]
    this_end = each_interval[1]
    if this_start <= new_interval[0]:
      op_list.append(each_interval)
      ### continue till interval is less than new interval

    else: 
      op_list.append(new_interval)
      op_list.extend(existing_intervals[i:])
      break 
  if len(op_list) == len(existing_intervals):
      op_list.append(new_interval)
      return op_list
  import pdb;pdb.set_trace()
  return merge_intervals(op_list)

insert_interval([[1,2],[3,4],[5,8],[9,15]] , [16,17])
