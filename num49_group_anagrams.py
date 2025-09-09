from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_table = {}
        for idx, string in enumerate(strs):
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams_table:
                anagrams_table[sorted_string].append(string)
            else:
                anagrams_table[sorted_string] = [string]
        anagrams = []
        for anagram in anagrams_table:
            anagrams.append(anagrams_table[anagram])
        return anagrams