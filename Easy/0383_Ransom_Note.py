"""
1.Ransom Note
Difficulty: Easy
Link:https://leetcode.com/problems/ransom-note/

Time Complexity: O(N)
Space Complexity: O(1)
Pattern: Hash Map
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters={}
        for letter in magazine:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        for second_letter in ransomNote:
            if second_letter in letters and letters[second_letter] > 0:
                letters[second_letter] -= 1
            else:
                return False
        return True
                
       
        
      