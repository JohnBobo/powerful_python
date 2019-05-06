def gen_squares(max_num):
    for num in range(max_num):
        yield num**2

MAX = 5

for square in gen_squares(MAX):
    print(square)
