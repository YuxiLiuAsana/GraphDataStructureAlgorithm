from typing import List
def floyd_warshall(m: List[List[float]]) -> List[List[float]]:
    v = len(m)
    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                m[j][k] = min(m[j][k], m[j][i] + m[i][k])
    return m