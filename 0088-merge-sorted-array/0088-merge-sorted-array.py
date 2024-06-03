class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        l = m + n - 1
        
        # While there are elements to process in nums2
        while l2 >= 0:
            if l1 >= 0 and nums1[l1] > nums2[l2]:
                nums1[l] = nums1[l1]
                l1 -= 1
            else:
                nums1[l] = nums2[l2]
                l2 -= 1
            l -= 1