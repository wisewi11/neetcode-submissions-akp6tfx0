from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modify the grid in-place:
        -1  : water, cannot be traversed.
         0  : treasure chest.
         INF: land that can be traversed (initially unknown distance).
        After running, each land cell contains the distance to the nearest treasure chest,
        or remains INF if no chest is reachable.
        """

        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        INF = 2 ** 31 - 1

        # Queue for multi-source BFS, starting from all treasure chests.
        q = deque()

        # 1. Initialize queue with all treasure locations (value == 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 2. Multi-source BFS
        # We expand from all treasures simultaneously. Each step increases distance by 1.
        while q:
            r, c = q.popleft()
            current_distance = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and if it's traversable land with INF (unvisited)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # Update distance for this land cell
                    grid[nr][nc] = current_distance + 1
                    # Push into queue to expand further
                    q.append((nr, nc))