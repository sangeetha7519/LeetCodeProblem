![Screenshot 2024-09-18 174053](https://github.com/user-attachments/assets/d4b4ae84-3fd1-4e75-8598-079f1d857773)
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x< 0:
            sign=-1
        else:
            sign=1 
        rev=0
        x=abs(x)
        for i in str(x):
            digits=x%10
            if rev > (INT_MAX - digits) // 10:
                return 0 
            rev=rev*10+digits
            x=x//10
        
        return rev * sign
        
