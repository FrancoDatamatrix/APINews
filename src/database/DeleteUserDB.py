from .DBMongoHelper import DBmongoHelper

class DeleteUserDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

       def delete_user_by_id(self, user_id):
        result = self.users_collection.delete_one({"id": user_id})
        return result.deleted_count > 0
