

"""
    设有n种不同面值的硬币，各硬币的面值存于数组中，现在要用这些硬币来找钱，问对任意钱数m(0<=m<=20001)，求最少硬币的找钱方法
    面值为 [1,2,5,10,20,50,100,500,1000]
"""
# import pysnooper


# @pysnooper.snoop()
def minCoin(array, m):
    ret = []
    arrayLen = len(array)
    for i in range(arrayLen-1, -1, -1):
        while m >= array[i]:
            # m -= array[i]
            ret.append(array[i])
            # m = m % array[i]
    return ret
            

if __name__ == "__main__":
    array = [1,2,5,10,20,50,100,500,1000]
    print(minCoin(array, 93))