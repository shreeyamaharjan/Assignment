import re
regex='^[0-9]+$'

def check(string):
    if( re.search(regex, string)):
        print("The string {} is number".format(string))

    else:
        print("The string {} is not number".format(string))

string=input("Enter any string : ")
check(string)


