class Solution:
    def minWindows(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # Pop from the left of the window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("infinity") else ""