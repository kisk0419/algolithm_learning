import queue

def bfs(maze, start_pos, goal_pos, N, M):
    INF = 100000000

    que = queue.Queue()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dist = []

    d = [INF] * M
    dist = [d.copy() for i in range(N)]

    que.put(start_pos)

    dist[start_pos[0]][start_pos[1]] = 0

    while not que.empty():
        p = que.get()
        if p == goal_pos:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#' and dist[nx][ny] == INF:
                que.put((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]] + 1
    return dist[goal_pos[0]][goal_pos[1]]

maze = [
    '#S######.#',
    '......#..#',
    '.#.##.##.#',
    '.#........',
    '##.##.####',
    '....#....#',
    '.#######.#',
    '....#.....',
    '.####.###.',
    '....#...G#'
    ]
N = 10
M = 10
start_pos = (0, 1)
goal_pos = (9, 8)

print(bfs(maze, start_pos, goal_pos, N, M))
