x = '*QQQ**Q*Q'

def Rotate(x):
    new = x[6:8]+ x[0:6] + x[-1]
    return new

print(Rotate(x))