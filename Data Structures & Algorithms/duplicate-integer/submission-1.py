class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sacrifice memory for speed
        #sets store unique values, cannot have dups
        hashset = set()

        #iterate over list, store current n in set
        # if exists, return. Else if complete, return false for no dups.
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
