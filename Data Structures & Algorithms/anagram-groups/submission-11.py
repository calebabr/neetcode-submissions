class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            s = s.lower()
            alpha = [0] * 26
            for char in s: 
                alpha[ord(char) - ord('a')] += 1
            alpha = tuple(alpha)
            d[alpha].append(s)
        return list(d.values())