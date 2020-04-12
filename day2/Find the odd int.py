def find_it(seq):
    return list(filter(lambda x: x[1] % 2 != 0, {num:seq.count(num) for num in seq}.items()))[0][0]
