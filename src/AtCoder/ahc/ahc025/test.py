li = list(range(10))
rep = 2
print(li[:-rep] + ([] if rep == 1 else li[-rep + 1:]))
