- Input: An integer array
- Output: An integer array where each element at an index equal to product of integers in the array except self.

Example:
`
input = [1,2,3,4];
output = [24, 12, 8, 6]
`

## Catch
Can't use division operator. Required solution is `O(n)`

## Approach
Used the approach from Neetcode's video. `The main idea is to maintain prefix and postfix products.`

1. Create an `ans` array that is the final answer.
2. Maintain two variables `prefix = 1` and `postfix = 1`. Both these values store products before and after the array at a particular index.
3. First run a loop from `0 to end of array` and store product before an element at an index.

```python
for i in range(0, len(nums)):
    ans[i]*=prefix
    prefix*=nums[i]
```

4. Same logic from the end to start. Multiplying values from the right left and multiply postfix product.

```python
for i in range(n-1, -1, -1):
            ans[i]*=postfix
            postfix*=nums[i]
```
## Analysis
Time complexity - `O(n)`
Memory - `O(n)` (including the returning ans array).


