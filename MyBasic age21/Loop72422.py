from ctypes.wintypes import PINT


def ss(a,b):
    for i in range(a,b+18):
        for j in range(1,13):
            print("{} x {} = {}".format(i,j,i*j))
        print("*" * 15)

ss(1,8)