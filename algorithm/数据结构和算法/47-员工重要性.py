

"""
    给定一个列表，其中的数据表示 员工编号、员工重要性、员工的下属。问某员工及其所有下属的重要性之和
    [
        [1, 5, [2,3]],
        [2, 3, []],
        [3, 4, []]
    ]
"""


class Employee:
    def __init__(self, id, importance, sub):
        self.id = id
        self.importance = importance
        self.sub = sub


def SumImportanceOfEmployee(emps):
    if not emps:
        return 0
    # if len(emps) == 1:
    #     return emps[0][1]
    table = {emp[0]: emp for emp in emps}

    stack = [emps[0]]
    value = 0
    while stack:
        employee = stack.pop()
        if employee[2] == []:
            value += employee[1]
        else:
            value += employee[1]
            for subs in employee[2]:
                stack.append(table[subs])
    print(value)





if __name__ == "__main__":
    # a = Employee(1, 5, [2,3])
    # b = Employee(2, 3, [])
    # c = Employee(3, 4, [])
    # emps = [a, b, c]

    emps = [
        [1, 5, [2,3]],
        [2, 3, []],
        [3, 4, []]
    ]

    SumImportanceOfEmployee(emps)