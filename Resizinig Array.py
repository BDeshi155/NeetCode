class Solution:
    def lastRemaining(self, n: int) -> int:
        element = 1
        remove_ints = list(range(1, n+1))

        flag = True
        while flag:
            if len(remove_ints) == 1:
                break

            i = 0
            while i < len(remove_ints):
                remove_ints.pop(i)
                i += 1

            if len(remove_ints) == 1:
                break

            i = len(remove_ints) - 1
            while i >= 0:
                remove_ints.pop(i)
                i -= 2

            if len(remove_ints) == 1:
                break

        return remove_ints[0]


sol = Solution()
res = sol.lastRemaining(5)
print(res)