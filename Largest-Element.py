# class Solution:
#     def largestElement(self, nums):
#         L=nums[0]
#         for i in range(len(nums)-1):
#             if nums[i]<nums[i+1]:
#                 L=nums[i+1]
#         return L 
class Solution:
    def largestElement(self, nums):
        L=float('-inf')
        for x in nums:
            if x>L:
                L=x
        return L 
n=[-4, -3, 0, 1, -8]
print(Solution().largestElement(n))
