class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        altura_linha_max = [max(linha) for linha in grid]
        altura_coluna_max = [max(coluna) for coluna in zip(*grid)]

        aumento_total = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                altura_min = min(altura_linha_max[r], altura_coluna_max[c])
                aumento = altura_min - grid[r][c]
                aumento_total += aumento

        return aumento_total