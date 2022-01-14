L = int(input())
C = int(input())
i = 1
while i <= L:
        j = 1
        while j <= C:
                if (i == L) and (j == C):
                        if (i % 2 == 0) and (j % 2 == 0) or (i % 2 == 1) and (j % 2 == 1):
                                print(1)
                        else:
                                print(0)
                j = j + 1
        i = i + 1
