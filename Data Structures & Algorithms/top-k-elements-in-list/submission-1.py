class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the K most frequent nums, so 2 most frequent or 3 most frequent etc in a slice, order not matter
        # iterate through array, assign each num to hashmap with counter
        # return k most frequent
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
