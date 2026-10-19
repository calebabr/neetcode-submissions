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
            # no collision, though different direct
            elif stack and (stack[-1] < 0) and (a > 0):
                stack.append(a)
            # same sign
            elif stack and (stack[-1] / abs(stack[-1]) != (a / abs(a))):
                stack.append(a)
            # no stack
            else:
                stack.append(a)
        return stack
