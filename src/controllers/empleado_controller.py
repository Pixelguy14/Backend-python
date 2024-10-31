from flask import jsonify, request
from services.empleado_service import EmpleadoService

class EmpleadoController:
    @staticmethod
    def get_all():
        empleados = EmpleadoService.get_all()
        return jsonify(empleados)
    
    @staticmethod
    def get_by_id(empleado_id):
        empleado = EmpleadoService.get_by_id(empleado_id)
        return jsonify(empleado)
    
    @staticmethod
    def create_empleado():
        data = request.get_json()
        response = EmpleadoService.create_empleado(data)
        return jsonify(response)
    # borrar, actualizar 