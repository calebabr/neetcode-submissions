class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and (stack[-1] / abs(stack[-1])) != (a / abs(a)): # different signs
                recent = stack.pop()
                if abs(recent) > abs(a):
                    stack.append(recent)
                elif abs(recent) < abs(a):
                    stack.append(a)
                else:
                    continue
            # same sign
            while stack and (stack[-1] / abs(stack[-1]) != (a / abs(a))):
                stack.append(a)
            # no stack
            if not stack:
                stack.append(a)
        return stack
