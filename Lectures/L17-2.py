def f(x):
    x = 600

def fL(L):
    L = [600]

def fL2(L):
    L2[0] = 600

if __name__ == "__main__":
    x = 500
    f(x)
    print(x)

    L = [500]
    fL(L)
    print(L)

    L = [500]
    fL2(L)
    print(L)



# local variables (f)
# Name              Address
# x                 @1000 --> @1020

# local variables (fL)
# Name              Address
# L                 @1040 --> @1100

# local variables (fL2)
# Name              Address
# L2                @1040

# global variables
# Name              Address
# __name__          @1080
# f                 @1060
# x                 @1000
# L                 @1040


# memory
# Address             Value
# 1000                500
# 1020                600
# 1040                [@1000]
# 1060                <function f>
# 1080                "__main__"
# 1100                [@1020]