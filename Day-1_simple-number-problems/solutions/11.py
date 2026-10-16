n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0 and int(i**0.5)**2 == i:
        print(i, end=" " )