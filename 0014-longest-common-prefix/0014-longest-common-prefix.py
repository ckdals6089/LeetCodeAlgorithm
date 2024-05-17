class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the array to bring the smallest and largest strings together
        strs.sort()
        
        # The longest common prefix of the array will be the common prefix of the             first and last strings
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]