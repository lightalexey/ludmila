N = 6
INF = 30000
W = [
    [0, 2, 4, INF, INF, INF],
    [2, 0, 9, 7, INF, INF],
    [4, 9, 0, 8, 1, INF],
    [INF, 7, 8, 0, 3, 1],
    [INF, INF, 1, 3, 0, 2],
    [INF, INF, INF, 1, 2, 0]
    ]
col = [i for i in range(N)]
ostov = []
for k in range(N-1):
  minDist = 1e10
  for i in range(N):
    for j in range(N):
      if col[i] != col[j] and W[i][j] < minDist:
        iMin = i
        jMin = j
        minDist = W[i][j]
  ostov.append ( (iMin, jMin) )
  c = col[jMin]
  for i in range(N):
    if col[i] == c:
      col[i] = col[iMin]
for edge in ostov:
  print ( "(", edge[0], ",",
               edge[1], ")" )