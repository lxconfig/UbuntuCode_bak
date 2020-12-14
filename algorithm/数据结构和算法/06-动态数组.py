import ctypes

class ArrayList:
    """动态数组"""
    def __init__(self):
        self._size = 10  # 动态数组的容量
        self._len = 0   # 动态数组当前大小
        self._list = (self._size * ctypes.py_object)()
    
    def isEmpty(self):
        """判空"""
        if self._len == 0:
            return True
        return False
    
    def isFull(self):
        """判满"""
        return self._size == self._len
    
    def length(self):
        """长度"""
        return self._len
    
    def getItem(self, index):
        """根据索引获取元素"""
        if index >= self._size or index < 0:
            # 索引位置不合法
            return "no value in %s index" % index
        return self._list[index]
    
    def append(self, value):
        """插入元素"""
        if self._len == self._size:
            # 数组满了, 重新开辟空间
            self.resize(2 * self._size)
        self._list[self._len] = value
        self._len += 1
    
    def resize(self, size):
        """重新开辟空间"""
        new_list = (size * ctypes.py_object)()
        for i in range(self._len):
            new_list[i] = self._list[i]
        self._list = new_list   # 指向新的数组空间
        self._size = size       # 修改位新的数组容量
    
    def insert(self, index, value):
        """按索引位置插入"""
        if index >= self._size or index < 0:
            # 插入的位置不合法，不能比数组容量还大，不能小于0
            return "can't insert index of %s" % index
        elif self.isFull():
            # 数组满了
            self.resize(2 * self._size)
        for i in range(self._len, index, -1):
            self._list[i] = self._list[i-1]
        self._list[index] = value
        self._len += 1
    
    def remove(self, value):
        """删除元素"""
        for i in range(self._len):
            if self._list[i] == value:
                # 找到了
                for j in range(i, self._len-1):
                    self._list[j] = self._list[j+1]
                self._list[self._len - 1] = None  # 把最后移走的那个位置置为None
                self._len -= 1
                return "remove %s success" % self._list[i]
        return "value not found"

    def pop(self, index):
        """按索引位置删除"""
        if index >= self._size or index < 0:
            # 删除位置不合法
            return "can't pop index of %s" % index
        value = self._list[index]
        for i in range(index, self._len - 1):
            self._list[index] = self._list[index+1]
        self._list[self._len - 1] = None
        return "pop %s success" % value

    def _print(self):
        for i in range(self._len):
            print(self._list[i], end=" ")
        print()

if __name__ == "__main__":
    array = ArrayList()
    print("初始时:")
    print("*" * 10)
    print("数组长度:", array._len)
    print("数组容量:", array._size)
    print("*" * 10)

    print("插入值:")
    array.append(0)
    array.append(1)
    array._print()
    print("*" * 10)
    
    print("insert插入值:")
    array.insert(2, 2)
    array.insert(3, 3)
    array._print()
    print("*" * 10)

    print("remove删除值:")
    array.remove(2)
    array._print()
    print("*" * 10)

    print("pop删除值:")
    array.pop(1)
    array._print()
    print("*" * 10)