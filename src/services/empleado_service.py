import bcrypt
from repositories.empleado_repository import EmpleadoRepository
from models.empleado_model import Empleado

class EmpleadoService:
    def __init__(self):
        self.repository = EmpleadoRepository()
    def get_all(self):
        return self.repository.get_all()
    
    def create_empleado(self, data):
        if self.repository.get_by_user(data['usuario']):
            raise ValueError('El usuario ya existe')
        
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed.decode('utf-8')

        empleadoNuevo = Empleado(**data)
        return self.repository.create_empleado(empleadoNuevo)
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    
    def get_by_user(self, username):
        return self.repository.get_by_user(username)

    def delete_empleado(self, id):
        return self.repository.delete_empleado(id)   
    
    def update_empleado(self, id, data):
        if 'password' in data:
            hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed.decode('utf-8')
        self.repository.update_empleado(id, data)