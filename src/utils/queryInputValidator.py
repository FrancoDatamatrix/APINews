class QueryValidator:
    @staticmethod
    def validate_user_data(user_data):
        # Verificar si se proporcionan el usuario, la contraseña, la hora y al menos una palabra
        if 'usuario' not in user_data or 'contraseña' not in user_data or 'hora' not in user_data or 'palabras' not in user_data or 'lugar' not in user_data:
            return False
        
        return True
     
