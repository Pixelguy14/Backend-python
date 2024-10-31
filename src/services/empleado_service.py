from repositories.empleado_repository import EmpleadoRepository
from utils.encryption_util import encrypt_password
from utils.token_util import generate_token
import time 

class EmpleadoService:
    @staticmethod
    def get_all():
        return EmpleadoRepository.get_all()
    
    @staticmethod
    def get_by_id(empleado_id):
        return EmpleadoRepository.get_by_id(empleado_id)
    
    @staticmethod
    def create_empleado(data):
        if EmpleadoRepository.get_by_user(data['usuario']):
            return {"error": "El Usuario ya Existe"}
        data['password'] = encrypt_password(data['password'])
        EmpleadoRepository.create_empleado(data)
        # Creamos el token despues de que se creo el usuario
        token = generate_token(data['usuario'])
        return {
            "message": "Empleado Registrado",
            "token": token
        }