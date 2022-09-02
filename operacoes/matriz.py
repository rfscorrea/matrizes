def somar(matriz1, matriz2):
    nova_matriz = {'i': matriz1['i'], 'j': matriz1['j']}

    for i in range(1, matriz1['i'] + 1):
        for j in range(1, matriz1['j'] + 1):
            a = matriz1[f'a{i}{j}']
            b = matriz2[f'b{i}{j}']
            c = a + b
            nova_matriz[f'c{i}{j}'] = c
    return nova_matriz


def subtrair(matriz1, matriz2):
    nova_matriz = {'i': matriz1['i'], 'j': matriz1['j']}

    for i in range(1, matriz1['i'] + 1):
        for j in range(1, matriz1['j'] + 1):
            a = matriz1[f'a{i}{j}']
            b = matriz2[f'b{i}{j}']
            c = a - b
            nova_matriz[f'c{i}{j}'] = c
    return nova_matriz


def escalar(matriz, n=1):
    nova_matriz = {'i': matriz['i'], 'j': matriz['j']}

    for i in range(1, matriz['i'] + 1):
        for j in range(1, matriz['j'] + 1):
            a = matriz[f'a{i}{j}']
            b = a * n
            nova_matriz[f'c{i}{j}'] = b
    return nova_matriz


def multiplicar(matriz1, matriz2):