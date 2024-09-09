from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for val in nums:
            if val-1 in num_set: continue
            count = 1
            while val+count in num_set:
                count += 1
            if count > longest: longest = count
        return longest