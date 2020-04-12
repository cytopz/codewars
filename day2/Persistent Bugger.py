from functools import reduce
def persistence(n):
    if len(str(n)) <= 1:
        return 0
    res = reduce(lambda x, y: x * y, [int(num) for num in list(str(n))])
    count = 1
    while len(str(res)) > 1:
        res = reduce(lambda x, y: x * y, [int(num) for num in list(str(res))])
        count += 1
    return count
