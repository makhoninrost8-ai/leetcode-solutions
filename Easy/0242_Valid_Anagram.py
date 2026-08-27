"""
1.  Valid Anagram
Difficulty: Easy
Link:https://leetcode.com/problems/valid-anagram/

Time Complexity: O(N)
Space Complexity: O(N)
Pattern: Hash Map, Sorting
"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else: 
                counter[char] = 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True