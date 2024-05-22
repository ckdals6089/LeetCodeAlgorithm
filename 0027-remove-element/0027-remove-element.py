class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the next position to place a non-val element
        next_pos = 0

        # Iterate over each element in the list
        for num in nums:
            # If the element is not equal to val, place it at the next position
            if num != val:
                nums[next_pos] = num
                next_pos += 1

        # Return the count of elements which are not equal to val
        return next_pos