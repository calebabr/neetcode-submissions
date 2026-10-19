from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        ingredRec = defaultdict(list)
        ingredNeed = {}
        visit = deque()
        visited = set()
        for s in supplies:
            visit.append(s)

        for i in range(len(recipes)):
            ingredNeed[recipes[i]] = len(ingredients[i])
            for j in ingredients[i]:
                ingredRec[j].append(recipes[i])
        
        recipes = set(recipes)
        while visit:
            curr = visit.popleft()
            if curr in recipes:
                res.append(curr)
            for rec in ingredRec[curr]:
                ingredNeed[rec] -= 1
                if ingredNeed[rec] == 0:
                    visit.append(rec)
        # print(ingredNeed)
        # print(visit)
        # print(ingredRec)
        return res     
            
        
