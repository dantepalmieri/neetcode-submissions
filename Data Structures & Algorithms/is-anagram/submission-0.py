class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strings are different length then can't be valid
        if len(s) != len(t):
            return False
        
        # sort strings and compare
        return sorted(s) == sorted(t)