class Solution:

    # Time complexity: O(n), Space complexity O(1)
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join([c.lower() for c in s if self.alphaNum(c)])
        
        # empty string is a palindrome
        if not new_str:
            return True

        n = len(new_str)
        mid = n // 2
        for i in range(mid+1):
            if new_str[i] != new_str[n-i-1]:
                return False
        return True
    
    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
    # Time complexity: O(n), Space complexity O(n)
    def isPalindromeBruteForce(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]