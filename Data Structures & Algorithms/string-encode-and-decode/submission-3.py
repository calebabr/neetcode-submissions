class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs: # for each string, append "#" followed by its length
            ans += f"{len(s)}#" + s
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): # iterate through the entire string
            j = i
            while s[j] != "#": # keep going until we find the #
                j += 1
            length = int(s[i:j]) # find the length from i to j
            res.append(s[j+1:j+1+length]) # single out just the word
            i = j + 1 + length # increment to after the added word
        return res

