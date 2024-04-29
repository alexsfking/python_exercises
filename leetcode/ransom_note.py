'''
### Easy ###
383. Ransom Note
Easy
Topics
Companies

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''

from collections import Counter

class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        magazine_dict = Counter(magazine)
        ransom_dict = Counter(ransom_note)
        for k, v in ransom_dict.items():
            if k not in magazine_dict or magazine_dict[k] < v:
                return False
        return True


r_n = "bg"
mag = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
s = Solution()
print(s.canConstruct(r_n, mag))