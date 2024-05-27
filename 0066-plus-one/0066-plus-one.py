class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move towards the first digit
        for i in reversed(range(len(digits))):
            print(i)
            # If the current digit is less than 9, increment it by 1 and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0
            digits[i] = 0
        
        # If all the digits were 9, we need to add a 1 at the beginning
        return [1] + digits
        