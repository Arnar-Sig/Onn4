


import queue


# def kbonacci(n, k):
#     rod = queue.Queue(k+1)
#     for x in range(k-1):
#         rod.put(0)
#     rod.put(1)


def kbonacci(n, k):
    arr = [0 for x in range(k-1)]
    arr.append(1)
    i = k
    while i < n:
        sum = 0
        for x in range(i-1, i-k-1, -1):
            sum += arr[x]
        arr.append(sum)
        i += 1
    print(k,"-bonacci runa med n:", n, arr)

for x in range(3, 9):
    kbonacci(20, x)
