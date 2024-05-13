from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class DeleteNewsDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def delete_news_by_id(self, news_id):
        # Convertir el ID de la noticia a ObjectId
        news_oid = ObjectId(news_id)

        # Eliminar la noticia por su ObjectId (_id)
        result = self.news_collection.delete_one({"_id": news_oid})

        return result.deleted_count > 0
