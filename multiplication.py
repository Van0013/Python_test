i = 1
print("-" * 50)
while i < 10:
    n = 1
    while n < 10:
        print("{:4d}".format(n * i), end = ' ')
        n += 1
    print()
    i += 1
print("-" * 50)

