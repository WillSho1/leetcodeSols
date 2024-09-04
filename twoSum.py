class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [nums_dict[target-nums[i]], i]
            nums_dict[nums[i]] = i
        return None