from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion

def main():
    #              acción   preecondiciones    efectos
    noop1 = Accion("noop1", ["at(o1 A)"],  ["at(o1 A)"])
    noop2 = Accion("noop2", ["in(o1 R)"],  ["in(o1 R)"])
    noop3 = Accion("noop3", ["-at(o1 A)"], ["-at(o1 A)"])
    noop4 = Accion("noop4", ["at(o1 R)"], ["-at(o1 R)"])
    noop5 = Accion("noop5", ["-at(o1 B)"], ["-at(o1 B)"])

    load_o1_R_A = Accion(  "load(o1 R A)",   ["at(o1 A)", "at(R A)"], ["in(o1 R)","-at(o1 A)"])
    unload_o1_R_A = Accion("unload(o1 R A)", ["in(o1 R)", "at(R A)"], ["at(o1 A)","-in(o1 R)"])
    unload_o1_R_B = Accion("unload(o1 R B)", ["in(o1 R)", "at(R B)"], ["at(o1 B)","-in(o1 R)"])
    load_o1_R_B = Accion(  "load(o1 R B)",   ["at(o1 B)", "at(R B)"], ["in(o1 R)","-at(o1 B)"])

    noop6 = Accion("noop6",   ["at(o2 A)"],  ["at(o2 A)"])
    noop7 = Accion("noop7",   ["in(o2 R)"],  ["in(o2 R)"])
    noop8 = Accion("noop8",   ["-at(o2 A)"], ["-at(o2 A)"])
    noop9 = Accion("noop9",   ["-in(o2 R)"], ["-in(o2 R)"])
    noop10 = Accion("noop10", ["at(o2 B)"],  ["at(o2 B)"])

    load_o2_R_A   = Accion("load(o2 R A)",   ["at(o2 A)", "at(R A)"], ["in(o2 R)", "-at(o2 A)"])
    unload_o2_R_A = Accion("unload(o2 R A)", ["in(o2 R)", "at(R A)"], ["at(o2 A)","-in(o2 R)"])
    unload_o2_R_B = Accion("unload(o2 R B)", ["in(o2 R)", "at(R B)"], ["at(o2 B)","-in(o2 R)"])
    load_o2_R_B   = Accion("load(o2 R B)",   ["at(o2 B)", "at(R B)"], ["in(o2 R)", "-at(o2 B)"])

    noop11 = Accion("noop11", ["at(R A)"],  ["at(R A)"])
    noop12 = Accion("noop12", ["-at(R A)"], ["-at(R A)"])
    noop13 = Accion("noop13", ["at(R B)"],  ["at(R B)"])
    noop14 = Accion("noop14", ["-fuel(R)"], ["-fuel(R)"])
    noop15 = Accion("noop15", ["-at(R B)"], ["-at(R B)"])

    fly_R_A_B = Accion("fly(R A B)", ["at(R A)", "fuel(R)"], ["-at(R A)", "at(R B)", "-fuel(R)"])
    fly_R_B_A = Accion("fly(R B A)", ["at(R B)", "fuel(R)"], ["-at(R B)", "at(R A)", "-fuel(R)"])

    noop16 = Accion("noop16", ["fuel(R)"], ["fuel(R)"])

    # lista de acciones
    acciones = [noop1, noop2, noop3, noop4, noop5, load_o1_R_A, unload_o1_R_A, unload_o1_R_B, load_o1_R_B, noop6,
    noop7, noop8, noop9, noop10, load_o2_R_A, unload_o2_R_A, unload_o2_R_B, load_o2_R_B, noop11, noop12, noop13,
    noop14, noop15, fly_R_A_B, fly_R_B_A, noop16]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print("| {0:40} | {1:50} |".format(accion, ", ".join(mutexs[accion])))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()
