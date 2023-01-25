import collections

N = 5*10**5 + 10
M = 3*10**3 + 10
MOD = 998244353

ans, n, m = 0, 0, 0
dp = [0] * N
obr = [0] * N
a = [0] * N
b = [0] * N
last = [0] * N

sum = [0] * N
lastupd = [0] * N
cur = [0] * N

pd = [collections.defaultdict(int) for i in range(N)]
que = [[] for i in range(N)]

n, m = map(int, input().split())

a = list(map(int, input().split())) * N
b = list(map(int, input().split())) * N
for i in range(1, m+1):
    obr[b[i]] = i
    lastupd[i] = -1

for i in range(1, n+1):

    if obr[a[i]] != 0:
        if last[a[i]] != -1:
            que[last[a[i]] - 1].append(obr[a[i]] - 1)
        que[i - 1].append(obr[a[i]] - 1)
    last[a[i]] = i

for i in range(1, n+1):
    last[a[i]] = 0

pd[0][0] = 1
for i in range(1, n+1):
    pd[0][i] = 1

for i in range(1, n+1):
    z = obr[a[i]]
    if z != 0:
        sum[z] = sum[z] + (((i - 1) - lastupd[z]) * cur[z]) % MOD
        sum[z] = sum[z] % MOD
        lastupd[z] = i - 1
        cur[z] = (pd[z - 1][i - 1] - pd[z - 1][last[a[i]] - 1] + MOD) % MOD
        pd[z][i] = sum[z] + cur[z]
    for u in que[i]:
        if lastupd[u] == -1:
            continue
        if u != 0:
            pd[u][i] = (sum[u] + ((i - lastupd[u]) * cur[u]) % MOD) % MOD
    last[a[i]] = i

print(m -1)
