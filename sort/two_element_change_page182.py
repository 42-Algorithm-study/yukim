N, K = map(int, input().split())
# N = int(N)
# K = int(K)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# for i in range(N):
#     A[i] = int(A[i])
#     B[i] = int(B[i])
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