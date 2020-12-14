

def main(k):
    """
        哥德巴赫猜想：任何一个大于2的偶数都可以写成两个质数的和
    """

    # O(n^2)的时间复杂度
    primes = [2, 3, 5, 7, 11, 13, 17]
    # k = 16   16 = 3+13
    '''
    for i in primes:
        b = k - i
        if b in primes:
            return "%s = %s + %s" % (k, i, b)
    '''
    # O(n)的时间复杂度 n代表primes列表的长度
    m, n = 0, len(primes)-1
    while m < n:
        if primes[m] + primes[n] < k:
            m += 1
        elif primes[m] + primes[n] > k:
            n -= 1
        else:
            return "%s = %s + %s" % (k, primes[m], primes[n])
    return "找不到"



if __name__ == "__main__":
    print(main(100))