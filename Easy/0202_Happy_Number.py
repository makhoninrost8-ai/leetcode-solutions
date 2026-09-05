class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        

        while n !=1:
            new_n=0
            for digit in str(n):
                new_n += int(digit)**2

            if new_n in seen:
                return False
            else:
                seen.add(new_n)
            n=new_n
        return True   
            