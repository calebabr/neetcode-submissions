class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids: # collision means stack is going right, new is left
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                top = stack[-1]
                if top > 0 and a < 0: # collision
                    if abs(top) > abs(a): # a gets destroyed
                        alive = False
                    elif abs(top) < abs(a): # a destroys top and moves on to next
                        stack.pop()
                    else: # both get destroyed
                        stack.pop()
                        alive = False
            if alive: # a has survived all collisions. add it
                stack.append(a)
        return stack
