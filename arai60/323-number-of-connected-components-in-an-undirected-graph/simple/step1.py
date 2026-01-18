# 12 / 41 testcases passed
class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        number_of_connected_components = 0
        for i in range(len(edges)):
            if i == 0:
                number_of_connected_components += 1
                continue
            if edges[i][0] == edges[i-1][-1]:
                continue
            number_of_connected_components +=1
        return number_of_connected_components
