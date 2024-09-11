def container_with_most_water(height):
    print(height)
    # Replace this placeholder return statement with your code
    
    end = len(height) - 1
    start = 0 
    this_val = 0 
    while start <=end :
        width = end - start
        this_val = max(this_val, min(height[start], height[end]) * width) 
        if height[start] <= height[end]:
            start += 1
        else:
            end = end -1 
      
    return this_val

input_ht = [7,7,2]
print(container_with_most_water(input_ht))
