from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        test_chr = ""
        num_chrs = 0
        end_search = False
        while True:
            for i,st in enumerate(strs):
                if st == "":
                    return ""
                if len(prefix) == len(st):
                    # print("Max possible prefix len reached")
                    end_search = True
                    break
                if i==0:
                    test_chr = st[len(prefix)]
                if len(st) > len(prefix) and prefix+test_chr == st[:len(prefix)+1]:
                    if i == len(strs)-1:  #Last string
                        prefix = prefix+test_chr
                        num_chrs += 1
                    else:
                        continue
                else:
                    # print("Test chr not found")
                    end_search = True
                    break
                
            if end_search:
                return prefix
            
        return prefix