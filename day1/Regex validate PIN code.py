def validate_pin(pin):
    #regex is bloat
    if not all(chr.isnumeric() for chr in pin): return False
    return len(pin) == 4 or len(pin) == 6
