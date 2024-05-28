class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize a list to store the binary sum
        result = []
        
        # Initialize carry to handle bit overflow
        carry = 0
        
        # Initialize pointers for a and b starting from the end of the strings
        i, j = len(a) - 1, len(b) - 1
        
        # Iterate while there are digits in a, b or carry is not zero
        while i >= 0 or j >= 0 or carry:
            # Get the current digit of a and b, or 0 if pointer is out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of the current digits and carry
            total = digit_a + digit_b + carry
            
            # Update the result with the current binary digit (total % 2)
            result.append(str(total % 2))
            
            # Update the carry (total // 2)
            carry = total // 2
            
            # Move the pointers to the left
            i -= 1
            j -= 1
        
        # Join the result list into a string and reverse it to get the correct order
        return ''.join(result[::-1])        