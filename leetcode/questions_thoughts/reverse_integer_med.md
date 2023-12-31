This was a straight forward question to reverse a given integer.

## Catches:
1. Always return 32-bit integer. i.e., check the size of the number before returning.

## Brute-Force Approach
1. Maintain a flag to check if the number is positive or negative. `flag = -1 if n < 0 else 1`.
2. Converting the number to string and then reverse the string using `string[::-1]`.
3. If the number is negative, the last char in the reversed string is `'-'`. Omit that string. _This can be checked based on the flag_.
4. Convert the string back to int and multiply the int with flag.
5. Final check to see if the reversed int is within 32-bit limit.
6. Return 0 if the limits are not met.

## Reversing each digit using `%`
1. Maintain a flag to check if the number is positive or negative. `flag = -1 if n < 0 else 1`.
2. Convert the number to positive while initializing flag itself. This is important as the '%' operators works differently for negative and positive numbers.
3. Start the reverse of number to be 0. While `n>=1`, calculate `rem = n%10`, use this rem to add to rev as `rev = (rev*10)+rem`. Within the while loop, update `n=n//10`.
4. Multiply the flag to the reversed number.
5. Finally, check if the reversed number is within the bounds and return.


