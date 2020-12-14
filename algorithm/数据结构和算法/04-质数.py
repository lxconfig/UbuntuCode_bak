import math


def is_prime_1(n):
    """
        找到n以内的质数，比如100以内的质数（质数也就是素数）
        性质：对于正整数n，如果去除以2-根号n之间所有的整数，均不能整除，则说明n是一个质数
    """
    # n = 100
    prime = []
    for i in range(2, n+1):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                # 可以整除，说明i不是质数
                break  # 跳出循环，进行下一个i值判断
            else:
                # 无法整除，说明i是质数
                prime.append(i)
                break  # 跳出循环
    print(" ".join(map(str, prime)))   # 输出格式：质数之间用一个空格隔开，最后一个不能有空格


def is_prime_2(n):
    array = []
    for i in range(2, n+1):
        array.append(i)
    
    primes = []
    not_primes = []
    


if __name__ == "__main__":
    is_prime_1(100)
    is_prime_2(10)