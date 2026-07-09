class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        currRows = len(matrix)
        # print("Row 1: ", matrix[0], " with total col ", len(matrix[0]))
        currCol = len(matrix[0])
        # print(currRows, ", ", currCol)
        newMat = [[0 for _ in range(currRows)] for _ in range(currCol)]
        for i in range(currRows):
            for j in range(currCol):
                newMat[j][i] = matrix[i][j]
        return newMat