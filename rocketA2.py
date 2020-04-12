from comprobar_mutex.accion import Accion
from comprobar_mutex.mutex import calcular_mutex_accion
# import json

def main():
    #              acción   preecondiciones    efectos
    noop1 = Accion("noop1", ["at(o1 A)"],  ["at(o1 A)"])
    noop2 = Accion("noop2", ["in(o1 R)"],  ["in(o1 R)"])
    noop3 = Accion("noop3", ["-at(o1 A)"], ["-at(o1 A)"])

    load_o1_R_A = Accion(  "load(o1 R A)",   ["at(o1 A)", "at(R A)"], ["in(o1 R)","-at(o1 A)"])
    unload_o1_R_A = Accion("unload(o1 R A)", ["in(o1 R)", "at(R A)"], ["at(o1 A)","-in(o1 R)"])
    unload_o1_R_B = Accion("unload(o1 R B)", ["in(o1 R)", "at(R B)"], ["at(o1 B)","-in(o1 R)"])

    noop4 = Accion("noop4", ["at(o2 A)"],   ["at(o2 A)"])
    noop5 = Accion("noop5", ["in(o2 R)"],  ["in(o2 R)"])
    noop6 = Accion("noop6", ["-at(o2 A)"], ["-at(o2 A)"])

    load_o2_R_A   = Accion("load(o2 R A)",   ["at(o2 A)", "at(R A)"], ["in(o2 R)", "-at(o2 A)"])
    unload_o2_R_A = Accion("unload(o2 R A)", ["in(o2 R)", "at(R A)"], ["at(o2 A)","-in(o2 R)"])
    unload_o2_R_B = Accion("unload(o2 R B)", ["in(o2 R)", "at(R B)"], ["at(o2 B)","-in(o2 R)"])

    noop7 = Accion( "noop7",  ["at(R A)"],  ["at(R A)"])
    noop8 = Accion( "noop8",  ["-at(R A)"], ["-at(R A)"])
    noop9 = Accion( "noop9",  ["at(R B)"],  ["at(R B)"])
    noop10 = Accion("noop10", ["-fuel(R)"], ["-fuel(R)"])

    fly_R_A_B = Accion("fly(R A B)", ["at(R A)", "fuel(R)"], ["-at(R A)", "at(R B)", "-fuel(R)"])
    fly_R_B_A = Accion("fly(R B A)", ["at(R B)", "fuel(R)"], ["-at(R B)", "at(R A)", "-fuel(R)"])

    noop11 = Accion("noop11", ["fuel(R)"], ["fuel(R)"])

    # lista de acciones
    acciones = [noop1, noop2, noop3, load_o1_R_A, unload_o1_R_A, unload_o1_R_B, noop4, noop5, noop6,
                load_o2_R_A, unload_o2_R_A, unload_o2_R_B, noop7, noop8 ,noop9, noop10, fly_R_A_B, 
                fly_R_B_A, noop11]

    # calcular mutex acciones
    mutexs = calcular_mutex_accion(acciones)

    # imprimir resultado
    for accion in mutexs:
        print("| {0:40} | {1:50} |".format(accion, ", ".join(mutexs[accion])))

    # print(json.dumps(mutexs, indent = 4))

    input("\nPulse enter para terminar")

if __name__ == "__main__":
    main()
