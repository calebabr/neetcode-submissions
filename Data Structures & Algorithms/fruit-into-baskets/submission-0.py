class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fruitCount = {}
        bestSize = 0
        for r in range(len(fruits)):
            fruitCount[fruits[r]] = fruitCount.get(fruits[r], 0) + 1
            while len(fruitCount) > 2:
                fruitCount[fruits[l]] -= 1
                if fruitCount[fruits[l]] == 0:
                    del fruitCount[fruits[l]]
                l += 1
            bestSize = max(bestSize, r - l + 1)
        return bestSize