import pysnooper

@pysnooper.snoop()
def num():
    a =  [lambda x, i=i: i*x for i in range(4)]
    return a
# print([m(2) for m in num()])

a = num()

for m in a:
    b = m(2)
    print(b)