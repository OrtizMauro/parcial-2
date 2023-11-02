def newSequence():
    
    lis = [] # Genero la lista.

    while len(lis) < 6:
        sequence = input("\nIngrese secuencia: ") # Ingreso secuencia valor por valor.
        if len(sequence) != 6:
            print("INGRESE LOS 6 VALORES CORRECTAMENTE DE LA SECUENCIA!")
            continue
        x = 0
        for i in sequence.upper():
            if (i == 'A') or (i == 'T') or (i == 'C') or (i == 'G'): # Valido los datos ingresados.
                x += 1
                if x == 6:
                    lis.append(sequence.upper()) # Lleno la lista.
                    print(lis) # Muestro los valores ingresados.
                    print(len(lis)) # Muestro la cantidad de valores ingresados.
            else:
                print("INGRESE SOLO UN VALOR QUE SEA 'A','T', 'C', 'G'") 
                

    return lis