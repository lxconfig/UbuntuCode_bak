
"""
"""

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance_1(self, employees: List['Employee'], id: int) -> int:
        queue, importances = [], 0
        queue.append(id)
        while queue:
            node = queue.pop(0)
            if node:
                for item in employees:
                    if item.id == node:
                        importances += item.importance
                        for nd in item.subordinates:
                            queue.append(nd)
        return importances
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {emp.id: emp for emp in employees}
        queue, value = [], 0
        queue.append(id)
        while queue:
            node = queue.pop(0)
            e = employee_dict[node]
            value += e.importance
            queue.extend(e.subordinates)
        return value
            
