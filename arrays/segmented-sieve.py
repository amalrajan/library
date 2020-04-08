import sys; sys.stdin = open(sys.path[0] + '\\input.txt', 'r'); sys.stdout = open(sys.path[0] + '\\output.txt', 'w')


def simple_sieve():
    mark = [False] * (n + 1)

    for i in range(3, n + 1, 2):
        if not mark[i]:
            primes.append(i)
            j = i * i
            while j <= n:
                mark[i] = True
                j += (2 * i)


def segmented_sieve(a, b):
    mark = [False] * n
    nsqrt = int(b ** 0.5)
    if a == 1:
        a += 1
    
    for p in primes:
        if p > nsqrt:
            break
        j = p * p  
        if j < a:
            j = ((a + p - 1) // p) * p
        
        while j <= b:
            mark[j - a] = True
            j += p

    for i in range(a, b + 1):
        if not mark[i - a]:
            print(i)


n = 10 ** 6 + 1
primes = [2]
simple_sieve()

for tc in range(int(input())):
    a, b = list(map(int, input().split()))
    segmented_sieve(a, b)
