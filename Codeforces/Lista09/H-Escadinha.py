n = int(input())
seq = list(map(int, input().split()))

if n < 3:
    print(1)
else:
    count = 1
    for i in range(2, n):
        if seq[i] - seq[i-1] != seq[i-1] - seq[i-2]:
            count += 1
    print(count)