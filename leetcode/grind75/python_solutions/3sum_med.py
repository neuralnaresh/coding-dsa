from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ## Brute Force (Working, but exceeding time limit)
        # ans = []
        # for k in range(len(nums)):
        #     val = nums[k]
        #     for i in range(len(nums)):
        #         for j in range(i+1, len(nums)):
        #             if i != k and j != k and i != j:
        #                 if nums[i]+nums[j] == -val:
        #                     if sorted([nums[i], nums[j], val]) not in ans:
        #                         ans.append(sorted([nums[i], nums[j], val]))

        ## Solution from Neetcode's video
        nums = sorted(nums)

        ans = []
        for i in range(len(nums)):

            if i > 0 and nums[i-1]==nums[i]:
                continue

            val = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r] > -val:
                    r-=1
                elif nums[l]+nums[r] < -val:
                    l+=1
                    # while nums[l]==nums[l-1] and l<r:
                    #     l+=1
                else:
                    ans.append([val, nums[l], nums[r]])

                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    r-=1
        return ans

if __name__ == "__main__":
    ans = Solution()
    l = [-1,0,1,2,-1,-4]
    print(ans.threeSum(l))