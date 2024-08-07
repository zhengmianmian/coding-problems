"""
This is not my solution, but better than mine.
"""
def solution(matrix):
    w, h = len(matrix[0]), len(matrix)
    rings = (min(w, h) + 1) // 2
    """
    get indexes of each ring
    """
    def ring(n):
        return [
            *((n, x) for x in range(n, w - n - 1)),
            *((y, w - n - 1) for y in range(n, h - n)),
            *((h - n - 1, x) for x in reversed(range(n + 1, w - n - 1)) if h - 1 > 2 * n),
            *((y, n) for y in reversed(range(n + 1, h - n)) if w - 1 > 2 * n),
        ]
    res = [[0] * w for _ in range(h)]
    for n in range(rings):
        ix = ring(n)
        print(ix)
        qq = ix[-1:] + ix[:-1] if n % 2 else ix[1:] + ix[:1]
        for (v, u), (y, x) in zip(qq, ix):
            res[v][u] = matrix[y][x]
    return res

m = [[ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]]

r = solution(matrix=m)