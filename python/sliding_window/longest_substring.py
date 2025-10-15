class Solution:

    # Time complexity: O(n), Space complexity O(n)
    # Sliding window technique
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res

    # Time complexity: O(n), Space complexity O(n)
    # Sliding window technique (optimal)
    def length_of_longest_substring_optimal(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(s[right] + 1, left)
            seen[s[right]] = right
            res = max(res, right - left + 1)
        return res

    # Time complexity: O(n^2), Space complexity O(n)
    def length_of_longest_substring_brute_foce(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            char_set = set()
            char_set.add(s[i])
            for j in range(i + 1, n):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            max_len = max(max_len, len(char_set))
        return max_len