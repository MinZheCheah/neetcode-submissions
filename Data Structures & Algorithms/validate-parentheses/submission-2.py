class Solution:
    def isValid(self, s: str) -> bool:
        # Brute Force
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
        
        # T: O(n^2)
        # S: O(n)



