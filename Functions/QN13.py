tup1 = [(1, 0), (4, 3), (2, 2), (5, 2), (9, 8)]
print("Original list of tuples:", tup1)
tup1.sort(key=lambda x: x[1])
print("Sorted list : ", tup1)
