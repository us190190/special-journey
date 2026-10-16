class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        first, second = -1, -1

        for i, num in enumerate(nums):

            if num == target:
                if first == -1:
                    first, second = i, i
                second = max(second, i)
        
        return [first, second]
        