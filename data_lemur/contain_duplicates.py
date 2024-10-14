def contains_duplicate(input)-> bool:
  ##return False
    import pdb;pdb.set_trace()
    if len(input) == len(set(input)):
        return True 
    else:
        return False

contains_duplicate([1, 3, 5, 7, 1])
