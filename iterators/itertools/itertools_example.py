from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = chunk(data, 3)

for chunk in chunks:
    print(chunk)
