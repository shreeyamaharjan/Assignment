def wordcount(string):
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1

        else:
            counts[word] = 1

    return (counts)


string = str(input("Enter any sentence : "))
print(wordcount(string))
