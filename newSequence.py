def newSequence():
    
    lis = [] # Genero la lista.

    while len(lis) < 36:
        sequence = input("\nIngrese secuencia: ") # Ingreso secuencia valor por valor.

        if (sequence.upper() == 'A') or (sequence.upper() == 'T') or (sequence.upper() == 'C') or (sequence.upper() == 'G'): # Valido los datos ingresados.
            lis.append(sequence.upper()) # Lleno la lista.
            
            print(lis) # Muestro los valores ingresados.
            print(len(lis)) # Muestro la cantidad de valores ingresados.

        else:
            print("INGRESE SOLO UN VALOR QUE SEA 'A','T', 'C', 'G'") 

    return lis