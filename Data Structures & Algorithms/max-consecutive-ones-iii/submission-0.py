class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start, end, rouge = 0, 0, 0
        max_len = 0

        while end<len(nums):
            if not nums[end]:
                rouge += 1

            while rouge>k and start<len(nums):
                if not nums[start]:
                    rouge -= 1
                start += 1
            
            cur_len = end - start + 1
            # print(f"s:{start} e:{end} l:{cur_len}, r:{rouge}")
            max_len = max(max_len, cur_len)
            end += 1
        
        return max_len

            





        