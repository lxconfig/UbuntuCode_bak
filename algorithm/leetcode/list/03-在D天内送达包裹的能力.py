

"""
    传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
    传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
    返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
"""


class Solution:
    def shipWithinDays(self, weights: list, D: int) -> int:
        """二分法
            假设船的运载能力为K
            1. 首先船的运载能力K至少要大于max(weights)，否则无法在D天内完成
            2. 若在一天内送完全部的货物，那么K=sum(weights)，也就是至少满足条件的K值（满足条件中K的最小值）
                则：K的取值范围：  max(weights) < K <= sum(weights)
            3. 对于某个运载能力K，判断K是否能在规定时间内完成送货任务
            
            细节：由于这个区间肯定是递增的，所以可以用二分法来加速寻找
        """
        if not weights or D == 0:
            return 0
        low, high = max(weights), sum(weights)
        if low == high:
            return low
        # 二分法
        while low < high:
            mid = (low + high) // 2
            if self.shipHelper(weights, D, mid):
                high = mid
            else:
                low = mid + 1
                # low += 1
        return low
    
    def shipHelper(self, weights, D, K):
        cur, day = K, 0   # cur表示当前船只还能运送的货物重量
        for weight in weights:
            if weight > K:
                # 若某个货物比运载能力还重，则这个K肯定是不满足条件的
                return False
            if cur < weight:
                # 若某个货物比当前船只能运送的重量还重，那么此货物不能运送
                # 重置cur，并且认为今天已经送完，day+1
                cur = K
                day += 1
            cur -= weight
        # 由于要到第二天才能day+1，所以会少一天
        day += 1
        return day <= D

        # cur = K
        # for weight in weights:
        #     if weight > K:
        #         return False
        #     if cur < weight:
        #         cur = K
        #         D -= 1
        #     cur -= weight
        # return D > 0


if __name__ == "__main__":
    s = Solution()
    weights = [3,2,2,4,1,4]
    print(s.shipWithinDays(weights, 3))
