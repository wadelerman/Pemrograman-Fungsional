from re import X


def pangkat(x, y):
    hasil = 1
    for y in range(y, 0, -1):
        hasil *= x
    print(hasil)

pangkat(5,5)