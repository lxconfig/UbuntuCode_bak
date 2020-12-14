

"""
    有N个活动，每个活动的开始时间为si， 结束时间是fi，如果si > fj 或者 sj > fi则说明两场活动不冲突
    找到有最多非冲突活动的集合

    思路：可以先对结束时间fi进行排序，然后判断当前活动的开始时间si是否大于前一个活动的结束时间fi
"""


def MaxActivities(array):
    sort_array = sorted(array, key=lambda li: li[1])
    prev = sort_array[0]
    print(prev)
    for cur in sort_array[1:]:
        if cur[0] >= prev[1]:
            print(cur)
            prev = cur


if __name__ == "__main__":
    array = [
        [0,6],
        [3,4],
        [1,2],
        [5,7],
        [8,9],
        [5,9]
    ]
    MaxActivities(array)