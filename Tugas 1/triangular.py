def triangular(number):
    list = (x for x in range(number+1))
    print(sum(i for i in list))

triangular(5)