def more_zeros(s):
    return list(dict(filter(lambda x: x[1].count('0') > x[1].count('1'), {k: bin(ord(k))[2:] for k in s}.items())).keys())
