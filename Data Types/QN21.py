a= [(1, 0), (4, 3), (2, 2), (5, 2), (9, 8)]

for j in range(1, len(a)):
    for i in range(len(a) - j):
        if a[i][1] > a[i + 1][1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
for i in range(len(a)):
    print(a[i])
