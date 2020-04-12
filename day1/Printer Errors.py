def printer_error(s):
    # regex is bloat
    err = len(list(filter(lambda x: x not in 'abcdefghijklm', s))) 
    return f'{err}/{len(s)}'
