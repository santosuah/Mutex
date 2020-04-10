from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion

def main():
    # definición                  lista            lista
    #               acción    preecondiciónes     efectos
    bake = Accion("bake(cake)", ["-have(cake)"], ["have(cake)"])
    noop1 = Accion("noop1", ["have(cake)"], ["have(cake)"])
    noop2 = Accion("noop2", ["-have(cake)"], ["-have(cake)"])
    eat = Accion("eat(cake)", ["have(cake)"], ["-have(cake)", "eaten(cake)"])
    noop3 = Accion("noop3", ["eaten(cake)"], ["eaten(cake)"])
    noop4 = Accion("noop4", ["-eaten(cake)"], ["-eaten(cake)"])

    # lista de acciones
    acciones = [bake, noop1, noop2, eat, noop3, noop4]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print(accion, "=>", ", ".join(mutexs[accion]))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()
