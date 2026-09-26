class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for i in range(len(s)):
                alpha[ord(s[i]) - ord('a')] += 1
            alpha = tuple(alpha)
            d[alpha].append(s)
        return list(d.values())