def is_mutant(dna):
    
    adn = [] # CREO UNA NUEVA LISTA PARA SEPARAR LOS CARACTERES.
    
    for i in dna:
        for j in i:
            adn.append(j) # AGREGO UNO POR UNO LOS CARACTERES.


    # Genero una matriz con la lista.
    mat = [[0 for _ in range(6)] for _ in range(6)]
    flag = 0
    for i in range(6):
        for j in range(6):
            mat[i][j] = adn[flag]
            flag += 1
    print("\nMATRIZ DE LA SECUENCIA:\n")
    
    #Se muestra la matriz.
    for row in mat:
       print(row)
    x = 0
    # Verifica si hay valores iguales en las diagonales de izquierda a derecha.
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i + 1][j + 1]) and (mat[i][j] == mat[i + 2][j + 2]) and (mat[i][j] == mat[i + 3][j + 3]):
                print("\nSe encontro una secuencia de valores iguales de izquierda a derecha")
                x += 1            


    # Verifica si hay valores iguales en las diagonales de derecha a izquierda.
    for i in range(3):
        for j in range(3, 6):
            if (mat[i][j] == mat[i + 1][j - 1]) and (mat[i][j] == mat[i + 2][j - 2]) and (mat[i][j] == mat[i + 3][j - 3]):
                print("\nSe encontro una secuencia de valores iguales diagonal de derecha a izquierda")
                x += 1
    
    
    # Verifica si hay valores iguales en una fila.
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1]) and (mat[i][j] == mat[i][j+2]) and (mat[i][j] == mat[i][j+3]):
                print("\nSe encontro una secuencia de valores iguales en una columna")                
                x += 1
    
    
    # Verifica si hay valores iguales en una columna.
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j]) and (mat[i][j] == mat[i+2][j]) and (mat[i][j] == mat[i+3][j]):
                print("\nSe encontro una secuencia de valores iguales en una columna")                
                x += 1
    
    if x >= 2:
        return True
    else:
        return False