class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        maxSum=float("-inf")
        curs=0
        for num in nums:
            curs+=num
            maxSum=max(maxSum,curs)
            if curs<0:
                curs=0
        return maxSum