


"""
    对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n， 100 <= m <= n <= 999
    如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开; 
    如果给定的范围内不存在水仙花数，则输出no; 每个测试实例的输出占一行。
"""

    
def findNarcissisticNumber(m, n):
    ret = []
    for i in range(m, n+1):
        target = helper(i)
        if target:
            ret.append(target)
    if len(ret) == 0:
        print("no")
    for j in ret:
        print(j, end=" ")

def helper(s):
    num = 0
    length = len(str(s))
    for i in str(s):
        num += int(i) ** 3
    if num == s:
        return s


def main():
    nm = list(map(int, input().split(" ")))
    m = nm[0]
    n = nm[1]
    
    findNarcissisticNumber(m, n)


if __name__ == "__main__":
    main()