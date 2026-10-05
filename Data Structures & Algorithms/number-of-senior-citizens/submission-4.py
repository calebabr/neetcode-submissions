class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            print(s[11:13])
            if int(s[11:13]) > 60:
                count += 1
        return count