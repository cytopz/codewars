def countBits(n):
    return len(list(filter(lambda x: x != '0', f'{n:b}')))
