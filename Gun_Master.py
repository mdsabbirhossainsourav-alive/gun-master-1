t = int(input())
for i in range(t):
    n,d = map(int, input().split())
    targets = list(map(int, input().split()))
    gun = 0  
    switches = 0
    for distance in targets:
        if distance <= d:
            needed = 0
        else:
            needed = 1
        if needed != gun:
            switches += 1
            gun = needed
    print(switches)
