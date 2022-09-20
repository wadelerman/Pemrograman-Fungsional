from re import X


def pangkat(x, y):
    hasil = 1
    for y in range(y, 0, -1):
        hasil *= x
    print(hasil)

def pangkat2(x,y):
    return x**y

pangkat(3, 2)
print(pangkat2(3, 9))