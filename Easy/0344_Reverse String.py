"""
1.  Reverse String
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Two Pointers

"""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left_pointer=0
        right_pointer=len(s) - 1
        while left_pointer < right_pointer:
            time = s[left_pointer]
            s[left_pointer] = s[right_pointer]
            s[right_pointer] = time
            left_pointer +=1
            right_pointer -=1

