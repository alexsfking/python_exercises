'''
### Easy ###
125. Valid Palindrome
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_string_list = []
        for c in s:
            if c.isalnum():
                converted_string_list.append(c.lower())
        s = ''.join(converted_string_list)
        return s == s[::-1]

s = Solution()
tests = ["A man, a plan, a canal: Panama", "race a car", " "]
for t in tests:
    print(s.isPalindrome(t))
