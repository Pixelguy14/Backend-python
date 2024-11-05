# port Empleado from empleado_model
from config.firebase_config import intialize_firebase
from models.empleado_model import Empleado

class EmpleadoRepository:
    def __init__(self):
        self.db = intialize_firebase()
        self.collection = self.db.collection('empleados_python')

    def get_all(self):
        empleados = [Empleado.from_dict(doc.to_dict()) for doc in self.collection.stream()]
        return empleados

    def create_empleado(self, empleado_nuevo):
        doc = self.collection.document()
        doc.set(empleado_nuevo.to_dict())
        return doc.id

    def get_by_user(self, username):
        docs = self. collection.where ("usuario","==",username).stream()
        for doc in docs:
            # retornamos un valor solo si encontramos un empleado con ese usuario
            return Empleado.from_dict(doc.to_dict())
        return None
    
    def get_by_id(self, id):
        doc = self.collection.document(id).get()
        return Empleado.from_dict(doc.to_dict()) if doc.exists else None 
    
    def update_empleado(self, id, data):
        self.collection.document(id).update(data)

    def delete_empleado(self, id):
        self.collection.document(id).delete()