from database.GetUserDB import GetUserDB

class GetUserRol:
    @staticmethod
    def get_user_role(usuario):
        get_user_db = GetUserDB()
        user = get_user_db.get_user(usuario)
        if user:
            return user["rol"]
        return None