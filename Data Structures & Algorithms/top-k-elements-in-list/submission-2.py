class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate over array
        # add num to map
        # everytime encounter that num, increment counter on it
        # somehow read from the map k highest.
        ans = []
        num_list = [[] for i in range(len(nums) + 1)]
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        for num, count in num_map.items():
            num_list[count].append(num)

        for i in range(len(num_list) -1, 0, -1):
            for num in num_list[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
