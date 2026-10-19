class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # collision
            if stack and (stack[-1]> 0) and (a < 0):
                recent = stack.pop()
                if abs(recent) > abs(a):
                    stack.append(recent)
                elif abs(recent) < abs(a):
                    stack.append(a)
                else:
                    continue
            # no stack or different direct (but no collision) or same sign
            else:
                stack.append(a)
        return stack
