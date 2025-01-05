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

    # hash table: time complexity O(n), space complexity O(N)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        
        return s_count == t_count

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
