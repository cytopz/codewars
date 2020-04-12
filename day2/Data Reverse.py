def data_reverse(data):
    new_arr = []
    for i in range(len(data), -1, -8):
        new_arr += (data[i:i+8])
    return new_arr
