import socket
import struct


def ip2int(address):
    ip_address = address.split(".")
    ret = 0
    for i in range(4):
        ret += int(ip_address[i]) * 256 ** (3 - i)
    return ret


def int2ip(num):
    lists = []
    for i in range(3, -1, -1):
        res = divmod(num, 256 ** i)
        lists.append(str(res[0]))
        num = res[1]
    return ".".join(lists)



if __name__ == "__main__":
    address = "192.168.2.10"
    print(ip2int(address))
    print(int2ip(3232236042))