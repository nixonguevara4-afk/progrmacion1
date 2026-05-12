def suma_matrices(A, B):
  resultado = []
  
  for i in range(len(A)):
     fila = []
     
     for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
            
  return resultado


def multiplicar_matrices(A, B):
    resultado = [[0] * len(B[0])for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


def producto_hadamard(A, B):
    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] * B[i][j])
        resultado.append(fila)

    return resultado


def producto_kronecker(A, B):
    resultado = []

    for fila_A in A:
        for fila_B in B:
            fila = []
            for elemento_A in fila_A:
                for elemento_B in fila_B:
                    fila.append(elemento_A * elemento_B)
            resultado.append(fila)

    return resultado