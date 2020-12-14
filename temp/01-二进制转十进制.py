

def bit2Decimal(s):
    if not s:
        return 0
    ret = 0
    pos = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == "1":
            ret += pow(2, pos)
            pos += 1
    return ret
    # return int(s)


def Decimal2Bit(s):
    if not s:
        return None
    # ret = ""
    # while s:
    #     ret += str(s % 2)
    #     s = s // 2
    # return ret[::-1]
    return "{:08b}".format(s)
    # return bin(s)


def octonary2Decimal(s):
    if not s:
        return 0
    # ret = 0
    # pos = 0
    # for i in range(len(s)-1, -1, -1):
    #     if s[i] == "1":
    #         ret += pow(8, pos)
    #         pos += 1
    # return ret
    return int(s)


def Decimal2Octal(s):
    if not s:
        return None
    # ret = ""
    # while s:
    #     ret += str(s % 8)
    #     s = s // 8
    # return ret[::-1]
    return oct(s)
    # return "{:04o}".format(s)


def Hex2Decimal(s):
    if not s:
        return None
    # ret = pos = 0
    # for i in range(len(s)-1, -1, -1):
    #     if s[i] == "1":
    #         ret += pow(16, pos)
    #         pos += 1
    # return ret
    return int(s)


def Decimal2Hex(s):
    # return hex(s)
    return "{:08x}".format(s)


if __name__ == "__main__":
    s = "0011"
    print(bit2Decimal(s))
    print(Decimal2Bit(10))
    print(octonary2Decimal(0o011))
    print(Decimal2Octal(10))
    print(Hex2Decimal(0x0011))
    print(Decimal2Hex(10))