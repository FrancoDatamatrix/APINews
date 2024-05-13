class InputValidator:
    @staticmethod
    def validate_user_data(user_data):
        if 'usuario' not in user_data or 'contraseña' not in user_data or 'api_key' not in user_data:
            return False
        return True
