def _print_data(data):
    '''
    配列データを文字列として表示する
    '''
    for d in data:
        print(*d)


def dfs(data, n, m):
    '''
    深さ優先の全検索クロージャー
    Wを再帰的に探索し、探索済みのノードは.に置きかえ再カウントされないようにする
    '''
    def _inner(x, y):
        # 今いる場所を.に置き換える
        data[x][y] = '.'
        # 今いる場所から隣接する8ノードでWのノードにのみ探索を行う
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 'W':
                    _inner(nx, ny)
        return
    return _inner


def get_lake_count(data, n, m):
    '''
    Wを深さ優先探索で総当たり
    '''
    f = dfs(data, n, m)

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'W':
                # Wが残っているならそこからdfsを始める
                f(i, j)
                count += 1
    return count


if __name__ == '__main__':
    N = 10
    M = 12
    input_data='''\
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
'''
    data = list(map(list, input_data.split('\n')))

    print('*** befor ***')
    _print_data(data)

    lake_count = get_lake_count(data, N, M)

    print('*** after ***')
    _print_data(data)

    print(lake_count)


