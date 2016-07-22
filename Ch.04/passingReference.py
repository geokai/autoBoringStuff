def eggs(someParameter, item):
    for x in item:
        someParameter.append(x)

spam = [1, 2, 3]
ham = [6, 5, 4]
print(spam)
eggs(spam, ham)
print(spam)

# comment
