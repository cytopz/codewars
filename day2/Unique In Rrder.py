def unique_in_order(iterable):
    res = []
    current = ''
    for letter in iterable:
        if letter != current: res.append(letter)
        current = letter
    return res
