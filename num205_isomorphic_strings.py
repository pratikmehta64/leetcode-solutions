class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translator = {}
        replacements = []
        for (s_c, t_c) in zip(s,t):
            if s_c not in translator:
                if t_c not in replacements:
                    translator[s_c] = t_c
                    replacements.append(t_c)
                else:
                    return False
            elif translator[s_c] != t_c:
                return False
        return True