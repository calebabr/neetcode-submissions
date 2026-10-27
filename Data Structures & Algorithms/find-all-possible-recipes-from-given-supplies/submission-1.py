from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        ingredRec = defaultdict(list)
        needs = {}
        visit = deque()

        for s in supplies:
            visit.append(s)
        
        for i in range(len(recipes)):
            needs[recipes[i]] = len(ingredients[i])
            for ingred in ingredients[i]:
                ingredRec[ingred].append(recipes[i])
            
        recipeSet = set(recipes)

        while visit:
            currIngred = visit.popleft()
            if currIngred in recipeSet:
                res.append(currIngred)
            for rec in ingredRec[currIngred]:
                needs[rec] -= 1
                if needs[rec] == 0:
                    visit.append(rec)
        
        return res
        
        
