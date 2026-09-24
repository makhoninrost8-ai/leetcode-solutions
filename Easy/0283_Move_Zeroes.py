"""
1.  Move Zeroes
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Two pointers

"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow=0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0
            
                
            

        
            
            

                

