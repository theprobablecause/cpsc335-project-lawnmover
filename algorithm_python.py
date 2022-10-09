# Let l be the provided list of 2n disks.

def lawnmower(n, l):
  iterations = int((n+1)/2)
  for it in range(iterations):
    # left to right
    for i in range(2*n-1):
      if l[i] == 1:
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
    # right to left
    for i in range(2*n-1, 0, -1):
      if l[i] == 0:
        temp = l[i]
        l[i] = l[i-1]
        l[i-1] = temp

def alternate(n, l):
  print(l)
  for i in range(n+1):
    for j in range(i, 2*n-1):
      if l[j] == 1:
        temp = l[j]
        l[j] = l[j+1]
        l[j+1] = temp


test = [0, 1, 0, 1, 0, 1, 0, 1]
n = 4
# lawnmower(n, test)
alternate(n, test)