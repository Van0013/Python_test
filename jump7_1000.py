for a in range(1001):
    if a % 7 == 0 or a % 10 == 7 or a // 100 == 7 or (a % 100 < 80 and a % 100 >= 70):
        continue
    else:
        print(a)
