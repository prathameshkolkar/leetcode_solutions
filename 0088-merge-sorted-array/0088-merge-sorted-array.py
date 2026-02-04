class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        
        for i in range(0,n):

            nums1.append(nums2[i])
            nums1.sort()
            if 0 in nums1:
                nums1.remove(0)         
                    
        """
        Do not return anything, modify nums1 in-place instead.
        """
        