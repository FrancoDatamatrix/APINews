import database.DBMongoHelper as DBMongoHelper
from api_service import APIService
# Función para validar las credenciales del usuario en MongoDB en Azure
#! Esto deberia ir en user_manager
def validar_credenciales(usuario, contraseña):

    # Consultar la base de datos para verificar las credenciales del usuario
    usuarios_collection = DBMongoHelper.usuarios
    usuario_encontrado = usuarios_collection.find_one({"usuario": usuario})

    # Verificar si se encontró un usuario con el nombre proporcionado
    if usuario_encontrado:

        # Comprobar la contraseña almacenada en la base de datos
        contraseña = usuario_encontrado['contraseña']
        return contraseña

    return False

def endpoint_query(request):
    try:
        # Obtener los datos de la solicitud
        request_data = request.json

        # Validar que se proporcionen datos en la solicitud
        if not request_data:
            raise ValueError("Los datos de la solicitud están vacíos")

        # Extraer la clave de API y las palabras
        api_key = request_data.get('api_key')
        palabras = request_data.get('palabras')

        # Validar que se proporcione una clave de API
        if not api_key:
            raise ValueError("API Key no proporcionada")

        # Validar que se proporcionen palabras y que al menos haya una
        if not palabras or len(palabras) == 0:
            raise ValueError("Debe proporcionar al menos una palabra")

        # Validar las credenciales del usuario en MongoDB en Azure
        usuario = request_data.get('usuario')
        contraseña = request_data.get('contraseña')
        if not usuario or not contraseña:
            raise ValueError("Usuario o contraseña no proporcionados")

        if not validar_credenciales(usuario, contraseña):
            raise ValueError("Credenciales de usuario incorrectas")

        # Simular la llamada al servicio y su método query
        servicio = APIService()
        resultado = servicio.query(api_key, palabras)

        return {"resultado": resultado}, 200
    except Exception as e:
        return {"error": str(e)}, 400
