def najmniejsza(*x):
    minimum: int = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    return minimum


print(najmniejsza(6, 2, 3, 10, 1000, 23))
