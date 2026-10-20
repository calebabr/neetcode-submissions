class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) of tuple(freq) to [words that match freq]
        ans = []
        freqs = defaultdict(list)

        for word in strs:
            freqChar = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                freqChar[idx] += 1
            freqChar = tuple(freqChar)
            freqs[freqChar].append(word)
        
        for f in freqs:
            ans.append(freqs[f])
        
        return ans