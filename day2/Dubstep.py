import re
def song_decoder(song):
    return re.sub('\s+', ' ', re.sub('(?i)wub', ' ', song)).strip()
