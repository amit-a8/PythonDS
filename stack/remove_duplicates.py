def remove_duplicates(s):
    
    stack = list()
    for each_char in s:
      if stack and each_char == stack[-1]:
        stack.pop()
      else:
        stack.append(each_char)
    return "".join(stack)

remove_duplicates("ggaabcdeb")
