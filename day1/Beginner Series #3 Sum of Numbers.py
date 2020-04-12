def get_sum(a,b):
    if a > b:
        return sum([x for x in range(a, b-1, -1)])
    return sum([x for x in range(a, b+1)])
