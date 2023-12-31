class Solution:
    def reverse(self, x: int) -> int:

        lowerbound = -2**31
        upperbound = 2**31-1

        if x > 0:
            sign = 1
        else:
            sign = -1
            x = -x

        ## Brute-Force Approach
        # string = str(x)
        # reversed_string = string[::-1]
        # rev_integer = sign*int(reversed_string)

        # if rev_integer >= lowerbound and rev_integer <= upperbound:
        #     return rev_integer
        # else:
        #     return 0

        # Reversing using % operator
        rev = 0
        while x >= 1:
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
    
        res = sign * rev
        if res >= lowerbound and res <= upperbound:
            return res
        else:
            return 0

if __name__ == "__main__":
    n = -123
    sol = Solution()
    print(sol.reverse(n))
