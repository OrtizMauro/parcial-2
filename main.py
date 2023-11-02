from newSequence import *
from isMutant import *

option = int(input("\nIngrese una opción: \n(1) Ingresar secuencia de ADN: \n(2) Salir: \n")) #MENU.
while True:
    if option == 1:
        lis = newSequence()
        
        if is_mutant(lis) == True: # Evalua si la funcio retorna true o false.
            print("\nRESULTADO DE LA SECUENCIA: -MUTANTE-\n")
        else:
            print("\nRESULTADO DE LA SECUENCIA: -NO MUTANTE-\n")

    elif option == 2: 
        break
    else:
        print("\nINGRESE UNA OPCION CORRECTA!") # Valida el ingreso de datos.
    option = int(input("\nIngrese una opción: \n(1) Ingresar nueva secuencia de ADN: \n(2) Salir: \n"))

    # CASO DE PRUEBA PARA QUE NO SEA MUTANTE: 
    # C T A G T G
    # C G C T C A
    # T A C A T G
    # A G C A T G
    # G C C T G A
    # T T A G G C
    
    # CASO DE PRUEBA PARA QUE SEA MUTANTE:
    # G A C A T G
    # C T A T T G
    # A T C C A T 
    # T T C A G A
    # A T A T C C
    # A A G C T T
