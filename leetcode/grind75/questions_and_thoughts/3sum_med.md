Description:

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j, i != k, and j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

- Input:
    - An integer array `nums`.

- Output:
    - Array containing triplets that sum to `0`.

## Brute Force
(Gives the right answer but exceeds the time limit)

Going through all combinations and adding triplets that sum to an `ans` list if they are not already present in `ans`.

```python
ans = []
for k in nums:
    for i in range(nums):
        for j in range(i to nums):
            if i != k and j != k and i != k:
                check the sum
                if sum:
                    sort the triplet array and check if not its in ans
                        if not there append
return ans
```

## Neetcode's solution
(The main idea is not to iterate over already checked combinations (i, j in triplet)).
1. First sort the `nums` array.
2. For i in `nums`, if i > 0 and nums[i] == nums[i-1], you already went through it, so continue
3. for each i, the solution now becomes `2Sum`.
4. Maintain two pointers `l=i+1` and `r=len(nums)-1`.
5. While `l<r` as the array is sorted, check if the sum `nums[l]+nums[r]` **exceeds** required sum, increase `l`, else decrease `r`.
6. else, the sum equals to required, so increment `l`, but we dont want to go through the same combination of l if the next value is same. Check this with a while loop and keep incrementing `l` until a new value at `l` is found.
7. Decrement `r`. (Does not change the correctness but decreases time complexity).

```python
nums = sorted(nums) # O(n^2) worst
ans = []
for i in nums:
    if i > 0 and i-1 has same value:
        continue
    
    initialize l and r
    while l < r:
        if sum exceeds required:
            l+=1
            check if l has same value and keep incrementing
        elif sum is below required:
            r-=1
            check if r has same value and keep decrementing
        else:
            append triplet to ans
            increment l
            check if l has same value and keep incrementing
            decrement r

return ans
```
