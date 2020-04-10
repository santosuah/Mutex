from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion

def main():
    # definición                  lista            lista
    #               acción    preecondiciónes     efectos
    noop1 = Accion("noop1", ["have(cake)"], ["have(cake)"])
    eat = Accion("eat(cake)", ["have(cake)"], ["-have(cake)", "eaten(cake)"])
    noop2 = Accion("noop2", ["-eaten(cake)"], ["-eaten(cake)"])

    # lista de acciones
    acciones = [noop1, eat, noop2]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print(accion, "=>", ", ".join(mutexs[accion]))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()
