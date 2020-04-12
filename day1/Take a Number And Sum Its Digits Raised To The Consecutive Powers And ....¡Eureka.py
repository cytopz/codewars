def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    def iseureka(num):
        res = 0
        for i, digit in enumerate(str(num), start=1):
            res += int(digit) ** i 
        return res == num
    return [x for x in range(a, b+1) if iseureka(x)]
