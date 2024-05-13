class UserManager:
    def __init__(self, user_db):
        self.user_db = user_db

    def create_user(self, user_data):
        """
        Crea un nuevo usuario con el correo y la contraseña proporcionados.

        Args:
        - email (str): El correo electrónico del nuevo usuario.
        - password (str): La contraseña del nuevo usuario.

        Returns:
        - str: El ID del nuevo usuario creado.
        """
        return self.user_db.create_user(user_data)