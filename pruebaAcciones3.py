from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion

def main():
    # definición
    #                       acción          preecondiciones           efectos
    noop1 = Accion(       "noop1",        ["at(o1 A)"],            ["at(o1 A)"])
    load_o1_R_A = Accion( "load(o1 R A)", ["at(o1 A)", "at(R A)"], ["in(o1 R)","-at(o1 A)"])
    noop2 = Accion(       "noop2",        ["at(o2 A)"],            ["at(o2 A)"])
    load_o2_R_A = Accion( "load(o2 R A)", ["at(o2 A)", "at(R A)"], ["in(o2 R)", "-at(o2 A)"])
    noop3 = Accion(       "noop3",        ["at(R A)"],             ["at(R A)"])
    fly_R_A_B = Accion(   "fly(R A B)",   ["at(R A)", "fuel(R)"],  ["-at(R A)", "at(R B)", "-fuel(R)"])
    noop4 = Accion(       "noop4",        ["fuel(R)"],             ["fuel(R)"])

    # lista de acciones
    acciones = [noop1, load_o1_R_A, noop2, load_o2_R_A, noop3, fly_R_A_B, noop4]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print(accion, "=>", ", ".join(mutexs[accion]))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()
