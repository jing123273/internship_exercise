M=int(input())
data=[]
for _ in range(M):
	N,S = input().split()
	S = int(S)
	data.append((N,S))

max_S = data[0][1]

for i in range(1, M):
    if data[i][1] > max_S:
        max_S = data[i][1]

for N, S in data:
	if S == max_S:
		print(N)