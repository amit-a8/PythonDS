def smallest_multiple(target: int) -> int:
    num = 1
    while True:
        for i in range(1, target + 1):
            if num % i != 0:
                num += 1
                break
            else:
                continue
        else:
            break
    return num

print(smallest_multiple(5))
