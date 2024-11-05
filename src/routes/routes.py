from flask import Blueprint
from controllers.empleado_controller import EmpleadoController
from middleware.auth_middleware import token_required

empleadoController = EmpleadoController()
routes = Blueprint('routes', __name__)

routes.add_url_rule('/empleados', 'get_all', empleadoController.get_all, methods=['GET'])
routes.add_url_rule('/empleados/<id>', 'get_by_id', empleadoController.get_by_id, methods=['GET'])
routes.add_url_rule('/empleados/user/<username>', 'get_by_user', empleadoController.get_by_user, methods=['GET'])
routes.add_url_rule('/empleados', 'create_empleado', empleadoController.create_empleado, methods=['POST'])
routes.add_url_rule('/empleados/<id>', 'delete_empleado', empleadoController.delete_empleado, methods=['DELETE'])
routes.add_url_rule('/empleados/<id>', 'update_empleado', empleadoController.update_empleado, methods=['PUT'])