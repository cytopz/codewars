import re
def solution(s):
    return [pair+'_' if len(pair) < 2 else pair for pair in re.findall('\w{1,2}', s)]
