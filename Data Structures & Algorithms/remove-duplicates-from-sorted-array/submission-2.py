class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# swapping array in place
# returning k
# two pointer solution
# if right is not unique, k moves
# we know first elem is always unique
# so we start at 1
        k = 1
        for r in range(1, len(nums)):
    #checking for uniqueness, if num[r] != num[r-1] it is unique
            if nums[r-1] != nums[r]:
                nums[k] = nums[r]
                # k is only iterating on unique nums
                k += 1
            
        return k
# careful of moving too fast and watch indents