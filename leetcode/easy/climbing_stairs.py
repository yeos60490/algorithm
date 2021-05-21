class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            steps = [1,2]
            for i in range(2,n):
                steps.append(steps[-1] + steps[-2])
        return steps[-1]
