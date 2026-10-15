class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and stack and  stack[-1] > 0 and a < 0: # collision; top of stack going right, curr a going left
                top = stack[-1]
                if abs(top) > abs(a): # a gets destroyed
                    alive = False
                elif abs(top) < abs(a): # top gets destroyed
                    stack.pop()
                else: # both destroyed
                    stack.pop()
                    alive = False
            if alive:
                stack.append(a)
        return stack
            