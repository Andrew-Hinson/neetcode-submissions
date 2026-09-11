class Solution:
    def minWindow(self, s: str, t: str) -> str:
# so the substring needs to be compared to the original string
# can be any order. Which makes me think of a set, however t and s could have dups so that may not work. 
# build hashmap, count freq of each char in each string
# return empty string if not there

        # str_map = {}
        # for char in t:
        #     str_map[char] = str_map.get(char, 0) + 1
        # ans_str = ""
        # for l in range(len(s)):
        #     compare_str = ""
        #     str_map_copy = str_map.copy()
        #     counter = len(t)

        #     if s[l] in str_map:
        #         r = l
        #         while counter > 0 and r < len(s):
                    
        #             # move r forward adding chars to ans regardless if found
        #             #iteration starts when s[l] in str_map is true
        #             # add chars to compare_str
        #             compare_str += s[r]
        #             # need to subtract from map if chars exausted
        #             # once exausted do a length check
        #             if s[r] in str_map_copy and str_map_copy[s[r]] > 0:
        #                 str_map_copy[s[r]] -= 1
        #                 counter -= 1
        #             if counter == 0:
        #                 if len(ans_str) == 0:
        #                     ans_str = compare_str
        #                 if len(compare_str) < len(ans_str):
        #                     ans_str = compare_str
        #             r += 1
            
        # return ans_str

        if t == "":
            return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
