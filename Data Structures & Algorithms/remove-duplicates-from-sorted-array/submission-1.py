class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sorted array
        # non decreasing order
        # remove duplicates IN PLACE
        # each element appears only once
        # return number of unique elements
        # [1,1,2,3,4]
        # [1,2,3,4]
        # return k = 4
        
        # plan
        # 2 pointer.
        # left, starts at 1
        # right, starts at 1
        # left only iterates if right is a unique num
        # why compare nums[right] to nums[right -1] and not to nums [left]
        # left starts at 1. New unique values are set where left is.
        # thats why we arent comparing to where left is.

        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left