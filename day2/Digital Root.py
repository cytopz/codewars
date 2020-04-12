def digital_root(n):
    if len(str(n)) <= 1:
        return n
    else:
        return digital_root(sum([int(num) for num in list(str(n))]))
