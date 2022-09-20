from unittest import result


def pangkat(x, y):
    for x in range(1, y+1):
        result = result*x
    return result

pangkat(3,5)

print(3*3)
print(sum(3*3 for x in range(1)))


