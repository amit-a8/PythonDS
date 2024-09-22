def next_greater_element(nums1, nums2):
    stack = []      
    map = {}        
    print(nums1)
    print(nums2)
    for current in nums2:
        while stack and current > stack[-1]:
            map[stack.pop()] = current
        stack.append(current)

    while stack:
        map[stack.pop()] = -1

    ans = []

    #or num in nums1:
    #   ans.append(map[num])
        
    return ans


print(next_greater_element([2, 4], [3, 2, 5]))
