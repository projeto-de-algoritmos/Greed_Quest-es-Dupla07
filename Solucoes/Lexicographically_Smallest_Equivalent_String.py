class UnionFind:
    def __init__(self, n):
        self.pais = [i for i in range(n)]
        self.tamanho = [1 for i in range(n)]

    def find(self, x):
        if self.pais[x] == x:
            return x
        else:
            return self.find(self.pais[x])

    def union(self, x, y):
        pai_x = self.find(x)
        pai_y = self.find(y)
        if pai_x != pai_y:
            if pai_x > pai_y:
                pai_x, pai_y = pai_y, pai_x
            self.pais[pai_y] = pai_x
            self.tamanho[pai_x] += self.tamanho[pai_y]

    def esta_conectado(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Cria um objeto UnionFind com 26 elementos (um para cada letra do alfabeto)
        uf = UnionFind(26)
        n = len(s1)

        # Faz a união das letras equivalentes de s1 e s2
        for i in range(n):
            uf.union(ord(s1[i])-ord('a'), ord(s2[i])-ord('a'))

        # Substitui cada letra de baseStr com sua letra equivalente (usando a função find)
        baseStr = list(baseStr)
        for i in range(len(baseStr)):
            baseStr[i] = chr(uf.find(ord(baseStr[i])-ord('a')) + ord('a'))

        # Retorna a baseStr modificada como uma string
        return "".join(baseStr)