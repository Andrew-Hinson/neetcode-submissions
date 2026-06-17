class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for n in nums:
            if n in dups:
                return True
            dups.update({n: 0})
        return False
        