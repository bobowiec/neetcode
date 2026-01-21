class Solution:

    # Time complexity: O(n), Space complexity O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(len1, len2):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - len1]) - ord('a')] -= 1
            if count1 == count2:
                return True

        return False

    # Time complexity: O(n*m), space complexity O(m)
    def checkInclusionWithHashMap(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        count = {}
        for k in s1:
            count[k] = count.get(k, 0) + 1
        
        for i in range(len2 - len1 + 1):
            sub_str = s2[i:i+len1]
            count_sub_str = {}
            for c in sub_str:
                count_sub_str[c] = count_sub_str.get(c, 0) + 1
            if count == count_sub_str:
                return True
        return False

    # Time complexity: O(n*m*lg(m)), Space complexity: O(m)
    def checkInclusionBruteForce(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        sorted_s1 = ''.join(sorted(s1))
        for i in range(len2 - len1 + 1):
            sub_str = s2[i:i+len1]
            sorted_sub_str = ''.join(sorted(sub_str))
            if sorted_s1 == sorted_sub_str:
                return True
        return False