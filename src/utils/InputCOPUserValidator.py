class InputValidator:
    
    REQUIRED_FIELDS = ['usuario', 'contraseña','rol']
    
    @staticmethod
    def validate_user_data(user_data):
        return all(field in user_data for field in InputValidator.REQUIRED_FIELDS)
