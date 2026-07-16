class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        s = 0
        e = len(people) - 1
        total = 0
        while s <= e:
            if people[s] + people[e] <= limit:
                s += 1
                e -= 1
            else:
                e -= 1
            total += 1
        return total
