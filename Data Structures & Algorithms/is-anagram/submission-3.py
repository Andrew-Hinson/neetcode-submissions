class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the cheap and easy method, returns true if they are equal
        #return sorted(s) == sorted(t)

        #understanding the problem 
        #hashmaps are good here to count frequency of characters 
        #check length first to rule out early exit, dif lengths can't be anagrams.
        if len(s) != len(t):
            return False

        #create empty dicts to serve as hashmaps
        countS, countT = {}, {}

        #iterate through each string, increment its assigned value, 
        #grab what is assigned to it first, default 0 if unseen.
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #iterate over counts and compare, note the .get(c,0) to avoid getting a null value
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True