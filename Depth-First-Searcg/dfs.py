def dfs(arr, index, sum, target):
    '''深さ優先探索
    部分和問題
    与えられた整数配列の要素の和がtargetと同じになるパターンがあるかを全検索で判定する
    '''
    if index == len(arr):
        return sum == target
    if dfs(arr, index+1, sum, target):
        return True
    if dfs(arr, index+1, sum+arr[index], target):
        return True
    return False

if __name__ == "__main__":
    A1 = [1,2,4,7]
    T1 = 13
    assert(dfs(A1, 0, 0, T1))
    
    A2 = [1,2,4,7]
    T1 = 15
    assert(not dfs(A1, 0, 0, T1))

