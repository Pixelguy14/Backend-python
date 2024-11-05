class Empleado:
    def __init__(self, id = None, nombre = '', apaterno= '', amaterno= '', direccion= '', telefono= '', ciudad= '', estado= '', usuario= '', password= '', rol= ''):
        self.id = id
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.direccion = direccion
        self.telefono = telefono
        self.ciudad = ciudad
        self.estado = estado
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Empleado(**data)