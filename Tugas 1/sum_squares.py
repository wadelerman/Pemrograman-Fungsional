def triangular(number):
    list = (x for x in range(number))
    listnew = sum(i for i in list)
    return listnew

data = triangular(5)
print(data)