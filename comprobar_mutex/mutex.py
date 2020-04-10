from .accion import Accion

def existe_efecto_inconsistente(accion1, accion2):
    
    # efecto de una acción niega el effecto de la otra
    for literal1 in accion1.efectos:
        for literal2 in accion2.efectos:
            if (literal1 == ("-" + literal2)) or (literal2 == ("-" + literal1)):
                return True
    return False


def existe_interferencia(accion1, accion2):

    # acción1 borra la precondición de accion2
    for literal1 in accion1.precondiciones:
        for literal2 in accion2.efectos:
            if ((literal1 == ("-" + literal2)) or (literal2 == ("-" + literal1))):
                return True

    # acción2 borra la precondición de accion1
    for literal1 in accion2.precondiciones:
        for literal2 in accion1.efectos:
            if  ((literal1 == ("-" + literal2)) or (literal2 == ("-" + literal1))):
                return True
    return False


def existe_competicion_recursos(accion1, accion2):

    # precondiciones mutuamente excluyentes
    for literal1 in accion1.precondiciones:
        for literal2 in accion2.precondiciones:
            if ((literal1 == ("-" + literal2)) or (literal2 == ("-" + literal1))):
                return True
    return False


def insertar_diccionario(clave, diccionario, tipo_mutex):

    if clave in diccionario:
        diccionario[clave] += [tipo_mutex]

    else:
        diccionario[clave] = [tipo_mutex]


def calcular_mutex_accion(lista_acciones):

    resultado = {}

    # comprobar todos los arcos de dos acciones
    # sin repetirlos
    for i in range(len(lista_acciones)):
    
        accion1 = lista_acciones[i]
    
        for j in range(i, len(lista_acciones)):
        
            accion2 = lista_acciones[j]

            # evitar accion con sigo misma
            if accion1.nombre_accion != accion2.nombre_accion:

                clave = accion1.nombre_accion + " + " + accion2.nombre_accion

                if existe_efecto_inconsistente(accion1, accion2):
                    insertar_diccionario(clave, resultado, "inconsistent_effect")

                if existe_interferencia(accion1, accion2):
                    insertar_diccionario(clave, resultado, "interference")

                if existe_competicion_recursos(accion1, accion2):
                    insertar_diccionario(clave, resultado, "competing_needs")

    return resultado
