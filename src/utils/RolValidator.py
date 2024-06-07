class RolValidator:
    @staticmethod
    def validate_rol(rol):
        # Verificar que el rol sea "Admin" o "User"
        return rol.lower() in ["admin", "user"]
