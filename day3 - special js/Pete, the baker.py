import math
def cakes(recipe, available):
    if len(available) < len(recipe):
        return 0
    else:
      remainder = {math.floor(available[k]/v):k for k, v in recipe.items()}
      return min(sorted(remainder, key=remainder.__getitem__))
