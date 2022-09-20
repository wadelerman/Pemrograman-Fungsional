def triangular(number):
    list = (x for x in range(number+1))
    listnew = sum(i for i in list)
    print(listnew)

triangular(5)