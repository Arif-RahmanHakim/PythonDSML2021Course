nums = [2,7,11,15]
target = 9 
class Solution:
    def twoSum(self, nums:List[int],target:List[int])-> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            return[]
