class Solution:

    def encode(self, strs: List[str]) -> str:
# I could use .join() to combine the list of strs to a string on the comma. Handle case where list of strs is empty str

        encoded_str = ""
        for s in strs:
        # int representing length + # as delimeter + string
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
# i could use .split() to put back into a list on comma
# handle case where input is empty str
        decoded_str, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_str.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return decoded_str