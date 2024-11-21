def gen01(idx, vector):
    if idx >= len(vector):
        print(vector)
        return

    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)


n = 2
vector = [None] * n
gen01(0, vector)