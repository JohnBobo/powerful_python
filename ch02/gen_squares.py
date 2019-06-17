def gen_squares(max_root):
    for n in range(max_root):
        yield n**2

MAX = 5
for square in gen_squares(MAX):
    print square
