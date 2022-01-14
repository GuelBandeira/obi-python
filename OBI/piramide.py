N = int(input())
matriz = [0] * N
for i in range(N):
	matriz[i] = [0] * N
for i in range(N):
	for j in range(N):
		matriz[i][j] = int(input())
peso = 0
retirada = N - 1 
i = 0
while i < N:
	j = 0
	while j < N:
		k = 0
		a = 0
		p = 1
		m = N - 1
		while p <= retirada:
			while k < N:
				if (k != j):
					if (matriz[i][j] >= matriz[i][k]):
						a = a + 1
				k = k + 1

			if (a == m):
				matriz[i][j] = 0
				m = m - 1
				if (m == -1):
					break
			p = p + 1
		j = j + 1
		if (j == N):
			j = 0
	retirada = retirada - 1
	i = i + 1
i = 0
soma = 0
while i < N:
	j = 0
	while j < N:
		soma = matriz[i][j] + soma
		j = j + 1
	i = i + 1
print(soma)