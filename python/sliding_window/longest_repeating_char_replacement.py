class Solution:

    # Time complexity: O(n), Space complexity: O(m)
    # Sliding window technique: O(26 * n)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

    # Time complexity: O(n), Space complexity: O(m)
    # Sliding window technique - optimal
    def characterReplacementOptimal(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res

    # Time complexity: O(n^2), Space complexity: O(m)
    # Brute force
    def characterReplacementBruteForce(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, max_freq = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                max_freq = max(max_freq, count[s[j]])
                if (j - i + 1) - max_freq <= k:
                    res = max(res, j - i + 1)
        return res