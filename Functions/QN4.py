def reverse(string):
    resulted_string = ""
    for i in string:
        resulted_string = i + resulted_string

    print("The reverse of the string is :", resulted_string)


string = input("Enter any string:")
print("The string  you entered is  :", string)
reverse(string)
