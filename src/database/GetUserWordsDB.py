from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class GetUserWordsDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def get_words(self, user_id):
        # Intentar convertir user_id a ObjectId
        try:
            user_oid = ObjectId(user_id)
            user = self.users_collection.find_one({"_id": user_oid})
            if user and "palabras" in user:
                palabras_string = user["palabras"]
                palabras_array = palabras_string.split(',')
                lugar = user.get("lugar")
                return palabras_array, lugar
            else:
                return None, None
        except:
            return None, None