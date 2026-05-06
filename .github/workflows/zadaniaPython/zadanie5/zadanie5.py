A = [1,2,3,4,5,6,7,8,9]
L = 12


znalezione = False
for i in A:
    if znalezione:
        break
    for j in A:
        if i + j == L:
            print(i, j, "Są równe ", L)
            znalezione = True
            