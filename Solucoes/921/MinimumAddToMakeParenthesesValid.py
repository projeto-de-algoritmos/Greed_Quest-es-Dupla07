class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        novosParenteses = 0
        equilibrio = 0

        for char in s:
            if char == '(':
                equilibrio += 1
            else:
                if equilibrio > 0:
                    equilibrio -= 1
                else:
                    novosParenteses += 1
            if equilibrio < 0:
                novosParenteses += abs(equilibrio)
                equilibrio = 0
        novosParenteses += equilibrio
        return novosParenteses