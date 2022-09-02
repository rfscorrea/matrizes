from operacoes import matriz

matrizes = [{}, {}]
matriz_soma = dict()

i0 = int(input('Linhas matriz 1: '))
j0 = int(input('Colunas matriz 1: '))
i1 = int(input('Linhas matriz 2: '))
j1 = int(input('Colunas matriz 2: '))

matrizes[0] = {'i': i0, 'j': j0}
matrizes[1] = {'i': i1, 'j': j1}


for i in range(1, i0+1):
    for j in range(1, j0+1):
        a = int(input(f'Entrada a{i}{j}: '))
        matrizes[0][f'a{i}{j}'] = a

for i in range(1, i1+1):
    for j in range(1, j1+1):
        b = int(input(f'Entrada b{i}{j}: '))
        matrizes[1][f'b{i}{j}'] = b
