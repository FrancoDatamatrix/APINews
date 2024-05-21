## Documentación De Usuario

### Introducción
La API REST de Creacion de noticias permite a los usuarios crear y almacenar noticias en base de datos diariamente de forma automatizada. A continuación, se detallan los pasos para utilizar la API.

### Uso Básico

#### Prerrequisitos
- Tener una cuenta en el sistema (credenciales).
- Herramientas recomendadas: curl, Postman, o cualquier cliente HTTP.



#### creacion de shedule
- **URL:** `api/v1/query`
- **Método:** `POST`
- **Descripción:** Crear un shedule para luego ser procesado y almacenado
- - **Cuerpo de la Solicitud:**
  ```json
  {
	"usuario":"usuario existente",
    "contraseña":"contraseña existente",
    "hora":1500, "(la hora debe estar en formato de 24 horas sin los ':', ejemplo 1500 para las 3 de la tarde)"
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