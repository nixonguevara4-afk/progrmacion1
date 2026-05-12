def ingresar_matriz():
  while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))

            if filas <= 0 or columnas <= 0:
                print("Error: las dimensiones deben ser positivas.")
                continue

            break

        except ValueError:
            print("Error: debe ingresar números enteros.")
            
        matriz = []
            
        for i in range(filas):
          while True:

            try:
                fila = list(map(float, input(f"Ingrese la fila {i+1}: ").split()))

                if len(fila) != columnas:
                    print("Error: cantidad incorrecta de elementos.")
                else:
                    matriz.append(fila)
                    break

            except ValueError:
                print("Error: solo se permiten números.")
                
          return matriz


def mostrar_matriz(A):

    for fila in A:
        for elemento in fila:
            print(f"{elemento:8.2f}", end=" ")

    print()