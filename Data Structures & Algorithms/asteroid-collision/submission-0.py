class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and (stack[-1] / abs(stack[-1])) != (a / abs(a)): # different signs
                recent = stack.pop()
                if abs(recent) > abs(a):
                    stack.append(recent)
                elif abs(recent) < abs(a):
                    stack.append(a)
                else:
                    continue
            # same sign
            elif stack and (stack[-1] / abs(stack[-1]) != (a / abs(a))):
                stack.append(a)
            # no stack
            else:
                stack.append(a)
        return stack
