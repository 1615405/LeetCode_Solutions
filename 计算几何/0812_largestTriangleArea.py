class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations
        def triangle_area(p1, p2, p3):
            import numpy as np
            matrix = np.array([p1 + [1], p2 + [1], p3 + [1]])
            return 0.5 * abs(np.linalg.det(matrix))
        
        return max(triangle_area(p1, p2, p3) for p1, p2, p3 in combinations(points, 3))