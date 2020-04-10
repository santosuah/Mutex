class Accion(object):

    def __init__(self, nombre_accion, precondiciones, efectos):
        self.nombre_accion = nombre_accion
        self.precondiciones = precondiciones
        self.efectos = efectos