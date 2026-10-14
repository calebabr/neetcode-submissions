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
                    elif abs(top) < abs(a): 
                        stack.pop()
                    else:
                        stack.pop()
                        alive = False
            if alive:
                stack.append(a)
            
        return stack
