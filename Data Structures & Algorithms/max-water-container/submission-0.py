class Solution:
    def maxArea(self, heights: List[int]) -> int:
    # ok so basically seems like a 2 pointer solution
    # possibly prefix array?
    # I could do 2 pointers
    # one pointer left, one pointer right
    # I get width = R - L times height, min(arr[L] * arr[R])
    # I store that value as a container value
    # every iteration I compare container value with new container value
    # it looks like I don't care about the new index even if the same,
    # so I would just output the container value for the ans
    # at what point do I move r over? I think thats the trick with this problem
    # move the pointer that has the smaller height val


    # create pointer
        r = len(heights) - 1
        l = 0
        volume = 0
        for buckets in heights:
            width = r - l
            height = min(heights[r], heights[l])
            volume = max(volume, width * height)
            if heights[r] > heights [l]:
                l += 1
            else:
                r -= 1

        return volume        