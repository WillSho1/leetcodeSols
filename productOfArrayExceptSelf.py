class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply forward
        prod = 1
        prod_list = [1]*len(nums)
        for ind, num in enumerate(nums):
            prod_list[ind] *= prod
            prod *= num

        # multiply backward
        prod = 1
        for ind in range(len(nums)-1, -1, -1):
            prod_list[ind] *= prod
            prod *= nums[ind]
        
        return prod_list
            
