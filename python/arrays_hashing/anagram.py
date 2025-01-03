class Solution:

    # brute force: time complexity O(n^2), space complexity O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i], '', 1)
            else:
                return False
        
        return True
    
    # sort: time complexity O(nlogn), space complexity O(1)
    def isAnagramSortedStrings(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

    # hash table: time complexity O(n), space complexity O(1)
    def isAnagramOpt(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1  
        
        for val in count:
            if val != 0:
                return False
        
        return True
