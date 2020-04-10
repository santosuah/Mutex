from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion

def main():
    # definición                  lista            lista
    #               acción    preecondiciónes     efectos
    a1 = Accion("a1", ["a"], ["b"])
    a2 = Accion("a2", ["-a"], ["c"])

    # lista de acciones
    acciones = [a1, a2]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print(accion, "=>", ", ".join(mutexs[accion]))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()