# port Empleado from empleado_model
import firebase_admin
from firebase_admin import credentials, firestore
coll = 'empleados_python'
from models.empleado_model import Empleado

cred = credentials.Certificate("RUTA_A_NUESTRO_ARCHIVO_FIREBASE")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = 'empleados_python'

class EmpleadoRepository:
    @staticmethod
    def get_all():
        empleados = db.collection(coll)
        return [doc.to_dict() for doc in empleados.stream()]
    '''
    @staticmethod
    def get_by_id(empleado_id):
        empleados = db.collection(coll)
        return [doc.to_dict() for doc in empleados.stream()]
    '''
    @staticmethod
    def create_empleado(data):
        db.collection(coll).add(data)

    @staticmethod
    def get_by_user(username):
        docs = db.collection(coll).where("usuario","==",username).stream()
        for doc in docs:
            # retornamos un valor solo si encontramos un empleado con ese usuario
            return Empleado.from_dict(doc.to_dict())
        return None