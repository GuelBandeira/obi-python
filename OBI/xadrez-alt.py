L=int(input('Defina o números de linha '))
C=int(input('Defina o números de colunas '))
vetor3=[0]*L #Vetor para qual o resultado FINAL vai ser jogado
vetor2=[0]*L #Vetor para guardar as linhas brancas
vetor1=[0]*L #Vetor para guardar as linhas pretas
m=[0]*L      # Matriz
for i in range(L):
    vetor3[i]=[0]*C
for i in range(L):
    vetor2[i]=[0]*C
for i in range(L):
    vetor1[i]=[0]*C #Atribuição de colunas e linhas às variaveis
for i in range(L):
    m[i]=[0]*C   
for i in range(L):
    for j in range(C):
            if i%2==0 and j%2==0:
                m[i][j]=0
            if j%2!=0 and i%2!=0: #Cálculo da parte preta
                m[i][j]=1
            if i%2!=0 and j%2!=0:
                m[i][j]=0
            if j%2==0 and i%2==0:
                m[i][j]=1
            vetor1[i][j]=m[i][j]
for i in range(L):
    for j in range(C):
            if i%2==0 and j%2==0:
                m[i][j]=0
            if j%2!=0 and i%2!=0: #Cálculo da parte branca
                m[i][j]=1
            vetor2[i][j]=m[i][j]
n=int(input("Deseja ver o tabuleiro ? 1 - Sim, 2 - Não "))
if n == 1:
    for i in range(L):
        for j in range(C):
            vetor3[i][j]=vetor1[i][j]+vetor2[i][j] # Soma das duas partes
            print(vetor3[i][j],end=' ')
        print()
    if vetor3[i][j]==0:
        print('A cor da posição digitada é : ',vetor3[i][j],'(preto)') 
    else:                                                             
        print('A cor da posição digitada é : ',vetor3[i][j],'(branco)')
else:                                                               #RESULTADO
    if vetor3[i][j]==0:
        print('A cor da posição digitada é : ',vetor3[i][j],'(preto)') 
    else:                                                             
        print('A cor da posição digitada é : ',vetor3[i][j],'(branco)')

