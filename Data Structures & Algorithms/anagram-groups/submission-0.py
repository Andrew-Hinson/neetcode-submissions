class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# i could construct a hashmap for each len of str
# then put each str assigned to a num.
# if c in str, its a match
# as i construct the map, I construct the final list 
# (dont want to iterate twice)

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
    # then we need to iterate over the map and build the list?
    # 2 iterations isnt great
