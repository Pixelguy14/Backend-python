from routes.empleado_rutes import init_empleado_routes
from middleware.auth_middleware import require_auth
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ventana_Arbol_Carro_Ave_Cielo'

#Inicializamos las rutas
init_empleado_routes(app)

#Definimos el middleware
app.before_request(require_auth)

if __name__ == "__main__":
    app.run(debub=True)