class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s1=sum(nums)
        s=n*(n+1)//2
        o=s-s1
        return o  

