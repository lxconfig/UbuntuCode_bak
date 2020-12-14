


def printMartix(array):
    for i in range(len(array)):
        row = []
        for j in range(len(array)):
            row.append(array[i][j])
        print(row)

class user:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "sssssss"


if __name__ == "__main__":
    array = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    printMartix(array)

    user = user("zs")
    print(user)