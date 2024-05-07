def mostrar_lista(una_lista:list, ilogico:int) -> bool:
    """Muestra una lista de numeros filtrando las posiciones que estan vacias
    Args:
        una_lista (list): La lista con los numeros
        ilogico (int): El valor de filtrado

    Returns:
        bool: True: Cuando esta todo OK | False: Cuando no recibio los tipos esperados
    """
    exito = False
    if type(una_lista) == list and type(ilogico) == int:
        exito = True
        for i in range(len(una_lista)):
            if una_lista[i] != ilogico: 
                print(f"{i + 1} -> {una_lista[i]}")
    
    return exito

def preguntar_seguir(mensaje: str, opcion):
    bandera_seguir = True
    seguir = input(mensaje)
    if seguir != opcion:
        bandera_seguir = False
    
    return bandera_seguir

def get_int(mensaje):
    numero = int(input(mensaje))
    return numero


def cargar_elemento(mi_lista, posicion, ilogico):
    exito = False
    if mi_lista[posicion] == ilogico: #si esta vacio    
        numero = get_int("Ingrese numero: ")
        mi_lista[posicion] = numero
        exito = True
    return exito   
###########################################################################
mi_lista = [-1] * 5

bandera_seguir = True
while bandera_seguir == True:
    posicion = get_int("Ingrese posicion: ")
    
    if cargar_elemento(mi_lista, posicion-1, -1) == False:
        print("Error, la posicion esta ocupada")
    
    bandera_seguir = preguntar_seguir("Quiere ingresar otro si/no", "si")

if mostrar_lista(mi_lista, -1) == False:
    print("Error al intentar mostrar la lista")
