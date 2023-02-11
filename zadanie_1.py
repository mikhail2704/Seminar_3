input()
list = map(int, (input().split()))
n = int(input())
a = 0
for i in list:
    if i == n:
        a += 1
print(a)