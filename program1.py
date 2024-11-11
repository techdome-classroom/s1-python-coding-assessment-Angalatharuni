class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Return 0 if the grid is empty
        if not grid or not grid[0]:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        visited_cells = [[False] * num_cols for _ in range(num_rows)]

        def explore_island(row, col):
            # Exit conditions for invalid or already visited cells
            if (
                row < 0 or row >= num_rows or
                col < 0 or col >= num_cols or
                grid[row][col] == 'W' or
                visited_cells[row][col]
            ):
                return
            # Mark the current cell as visited
            visited_cells[row][col] = True
            # Recursively visit adjacent cells
            explore_island(row - 1, col)  # up
            explore_island(row + 1, col)  # down
            explore_island(row, col - 1)  # left
            explore_island(row, col + 1)  # right

        total_islands = 0

        for row in range(num_rows):
            for col in range(num_cols):
                # Start a new exploration if an unvisited landmass is found
                if grid[row][col] == 'L' and not visited_cells[row][col]:
                    explore_island(row, col)
                    total_islands += 1  # Count this as a distinct island

        return total_islands
