n, m = list(map(int, input().split()))
N = set()
M = set()

for i in range(n + m):
    num = int(input())
    if n > 0:
        n -= 1
        N.add(num)
    else:
        m -= 1
        M.add(num)

intersection = N & M

for num in intersection:
    print(num)