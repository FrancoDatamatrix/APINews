# API REST de Creacion Noticias

## Documentación Técnica

### Introducción
Esta documentación describe la API REST para nuestro servicio de busqueda y creacion de noticias. La API permite a los usuarios crear y almacenar las noticias mas actuales en base de datos diariamente de forma automatizada

### Endpoints

#### 1. creacion/actualizacion de usuarios (Admin)
- **URL:** `/api/v1/create-update-users`
- **Método:** `POST`
- **Descripción:** Crear o actualizar usuarios con el uso de un token
- - **Cuerpo de la Solicitud:**
  ```json
  {
    "usuario": "nombre de usuario o email",
    "contraseña": "contraseña",
    "api-key": "{{md5Hash}}","(*no modificar* hash generado automaticamente con postman)"
  }

- **Respuesta Exitosa:**
  - **Código:** 201
  - **Cuerpo:**
    ```json
    {
    "message": "Usuario creado exitosamente",
    "user_id": "664be9fc6a867d1a853d6581"
    }
    ```



#### 2. eliminacion de usuarios (Admin)
- **URL:** `/api/v1/delete-user`
- **Método:** `DELETE`
- **Descripción:** Elimina un usuario
- **Cuerpo de la Solicitud:**
  ```json
  {
    "id": "el id del usuario a eliminar",
    
  }

- **Respuesta Exitosa:**
  - **Código:** 201
  - **Cuerpo:**
    ```json
   {
    "deleted_schedules_count": 0, "(ademas elimina los schedules asociados al usuario)"
    "message": "Usuario eliminado exitosamente",
    "user_id": "664be9fc6a867d1a853d6581"
}
    ```

#### 3. creacion de shedule
- **URL:** `api/v1/query`
- **Método:** `POST`
- **Descripción:** Crear un shedule para luego ser procesado
- - **Cuerpo de la Solicitud:**
  ```json
  {
	"usuario":"usuario existente",
    "contraseña":"contraseña existente",
    "hora":"15:00", "(la hora debe estar en formato de 24 horas)"
	"palabras":"termino a buscar",
    "lugar":"CO", "(codigo pais de dos letras, ejemplo CO para colombia)"
}
**visite la lista de paises disponibles en https://developers.google.com/custom-search/docs/json_api_reference?hl=es-419#countryCodes** 

- **Respuesta Exitosa:**
  - **Código:** 200
  - **Cuerpo:**
    ```json
    {
    "mensaje": "Petición recibida correctamente",
    "schedule_id": "664bf6c3952d7186e2a6dd56"
    }
    ```