from collections import deque

def flood_fill_bfs(grid, sr, sc, new_color):

    if not grid or grid[sr][sc] == new_color:
        return grid

    rows, cols = len(grid), len(grid[0])
    original_color = grid[sr][sc]


    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((sr, sc))
    grid[sr][sc] = new_color  

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original_color:
                grid[nr][nc] = new_color
                queue.append((nr, nc))

    return grid


if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    sr, sc = 1, 1
    new_color = 2

    result = flood_fill_bfs(image, sr, sc, new_color)
    for row in result:
        print(row)