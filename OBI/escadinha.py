while 1 > 0:
	N = int(input())
	if (N >= 1) and (N <= 1000):
		break
sequencia = [0] * N
for i in range(N):
	sequencia[i] = int(input())
i = N - 1
qt = 0
i = N - 1
if (N > 1):
	while i > 0:
		if (sequencia[i] > sequencia[i - 1]):
			if (i == N - 1):
				nn = sequencia[i] - sequencia[i - 1]
				qt = qt + 1
			else:
				if (sequencia[i] - sequencia[i - 1] != nn):
					qt = qt + 1
					nn = sequencia[i] - sequencia[i - 1]
		else:
			if (i == N - 1):
				nn = sequencia[i - 1] - sequencia[i]
				qt = qt + 1
			else:
				if (sequencia[i - 1] - sequencia[i] != nn):
					qt = qt + 1
					nn = sequencia[i - 1] - sequencia[i]

		i = i - 1
else:
	qt = qt + 1
print(qt)


