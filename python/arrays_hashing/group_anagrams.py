from typing import List


class Solution:

    # hash table with sorted word as they key, time complexity O(m * nlogn), space complexity O(m*n)
    # where: m is the number of strings and n is the length of the longest string
    def groupAnagramsWithSorting(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        
        return anagrams.values()
    
    # hash table: time complexity O(m * n), space complexity O(n)
    # where: m is the number of strings and n is the length of the longest string
    def groupAnagramsOpt(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26 # only lowercase letters from a to z
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count) # convert list to tuple to use it as a key
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        
        return anagrams.values()