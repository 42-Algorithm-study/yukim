N, K = input().split()
N = int(N)
K = int(K)

A = input().split()
B = input().split()
for i in range(N):
    A[i] = int(A[i])
    B[i] = int(B[i])
A.sort()
B.sort(reverse=True)
for i in range(K):
    tmp = A[i]
    if A[i] < B[i]:
        A[i] = B[i]
        B[i] = tmp

print(N, K)
print(A)
print(B)
print(sum(A))