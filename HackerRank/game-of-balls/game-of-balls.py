import sys

n = int(input())
radii = list(map(int, input().split()))

for k in range(1, n + 1):
  expected_balls = 0
  for i in range(1, n + 1):
    if i == k:
      expected_balls += 1
    else:
      expected_balls += radii[i - 1] / (radii[i - 1] + radii[k - 1])
  print('%.6f' % expected_balls)