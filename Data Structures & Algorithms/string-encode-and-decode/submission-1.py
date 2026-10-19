class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs)):
            ans += strs[i] + "0"
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        curr = ""
        dec = []
        for i in range(len(s)):
            if s[i] != "0":
                curr += s[i]
            else:
               dec.append(curr)
               curr = "" 
        return dec

