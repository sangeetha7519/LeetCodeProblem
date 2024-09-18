![Screenshot 2024-09-18 174053](https://github.com/user-attachments/assets/442e9da5-0512-41e8-be62-699e3f275271)
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
        
