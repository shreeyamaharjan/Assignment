def add_tags(tag, string):
    return "<%s>%s<!%s>" % (tag, string, tag)


string = str(input("Enter any string : "))
tag = str(input("Enter any HTML tag : "))

print(add_tags(tag, string))
