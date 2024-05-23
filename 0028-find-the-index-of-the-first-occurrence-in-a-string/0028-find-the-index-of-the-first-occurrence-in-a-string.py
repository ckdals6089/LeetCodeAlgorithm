class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is empty, return 0 as per problem definition
        if not needle:
            return 0
        
        # Get the length of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Iterate through the haystack up to the point where the remaining substring can still contain the needle
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring from the current position matches the needle
            if haystack[i:i+needle_len] == needle:
                return i
        
        # If the needle is not found in the haystack, return -1
        return -1        