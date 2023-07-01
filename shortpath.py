from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])  # (row, column, path length)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while queue:
            row, col, path_len = queue.popleft()
            if row == col == n - 1:
                return path_len
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col] and grid[new_row][new_col] == 0:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, path_len + 1))
        
        return -1

# Example usage
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

solution = Solution()
path_length = solution.shortestPathBinaryMatrix(grid)
print("Shortest clear path length:", path_length)
