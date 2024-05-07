def es_cuadrado_magico(matriz):
    if len(matriz) == len(matriz[0]):
        if elementos_diferentes(matriz):
            suma = sum(matriz[0])

            for i in range(1, len(matriz)):
                if suma != sum(matriz[i]):
                    return False
            
            for j in range(len(matriz[0])):
                suma_columna = sum([matriz[i][j] for i in range(len(matriz))])
                if suma != suma_columna:
                    return False

            suma_diagonal_principal = sum([matriz[i][i] for i in range(len(matriz))])

            if suma != suma_diagonal_principal:
                return False
            
            columnas = len(matriz[0]) - 1
            suma_diagonal_secundaria = 0
            for i in range(len(matriz)):
                suma_diagonal_secundaria += matriz[i][columnas]
                columnas -= 1
            
            return suma == suma_diagonal_secundaria
        else:
            return False
    else:
        return False
