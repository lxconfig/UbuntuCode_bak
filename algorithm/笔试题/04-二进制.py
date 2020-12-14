

def main(m):
    count = 0
    for i in range(1, m):
        ret = "{0:04b}".format(i)
        if isMatch(ret):
            count += 1
    print(count)

def isMatch(ret):
    if ret == ret[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    m = int(input())
    main(m)
    # print("{0:04b}".format(7))