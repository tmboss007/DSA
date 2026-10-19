class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char

        reversed_string = cleaned[::-1]

        return cleaned == reversed_string