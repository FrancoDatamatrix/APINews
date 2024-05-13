class InputDeleteValidator:
    @staticmethod
    def validate_id_user_data(user_id):
        if not 'user_id':
            return False
        return True
