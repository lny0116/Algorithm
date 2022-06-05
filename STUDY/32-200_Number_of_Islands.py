# 389 ms	16.7 MB
# https://leetcode.com/problems/number-of-islands/

def numIslands(grid: list[list[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid,i,j)
                count  += 1
    return count

def dfs(grid,i,j):
    grid[i][j] = 0
    for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
        r = i + dr
        c = j + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
            dfs(grid,r,c)


print(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

# 책 및 의견 참고