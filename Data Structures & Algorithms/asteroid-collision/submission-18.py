class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        moving = []
        for a in asteroid:
            status = True
            while status and moving and moving[-1] > 0 and a < 0:
                top = moving[-1]
                # top wins, a is nonStatus
                if top > abs(a):
                    status = False
                # a wins, remove top
                elif top < abs(a):
                    moving.pop()
                # no win, a is nonstatus and remove top
                else:
                    status = False
                    moving.pop()
            # if a is good status, add to moving
            if status:
                moving.append(a)
        return moving
