from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)

        ans = [1 for i in range(n)]

        for i in range(0, n):
            ans[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            ans[i]*=postfix
            postfix*=nums[i]

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.productExceptSelf(nums))