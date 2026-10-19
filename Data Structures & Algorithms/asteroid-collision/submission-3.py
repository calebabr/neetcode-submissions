class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # top is going left and new is going right means collision
            if stack and (stack[-1] / abs(stack[-1]) == 1) and (a / abs(a) == -1):
                recent = stack.pop()
                if abs(recent) > abs(a):
                    stack.append(recent)
                elif abs(recent) < abs(a):
                    stack.append(a)
                else:
                    continue
            # top is going right and new is going left means nothing
            elif stack and (stack[-1] / abs(stack[-1]) == -1) and (a / abs(a) == 1):
                stack.append(a)
            # same sign
            elif stack and (stack[-1] / abs(stack[-1]) != (a / abs(a))):
                stack.append(a)
            # no stack
            else:
                stack.append(a)
        return stack
