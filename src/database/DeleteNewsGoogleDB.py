import logging
import os
from flask import g
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class DeleteNewsDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        # self.news_collection = self.db_helper.get_collection("news")
                      
    def delete_news_by_id(self, selected_news):
        try:
            # Obtener todas las bases de datos
            databases = self.client.list_database_names()

            results = []

            for news_item in selected_news:
                group_id = news_item['group_id']
                news_ids = [news_item['news_id']]  # news_ids debe ser una lista

                # Convertir el ID del grupo de noticias a ObjectId
                group_oid = ObjectId(group_id)

                for db_name in databases:
                    db = self.client[db_name]
                    if "news" in db.list_collection_names():
                        news_collection = db["news"]

                        # Eliminar las noticias anidadas que contienen los ObjectIds en su campo "_id"
                        result = news_collection.update_one(
                            {"_id": group_oid},
                            {"$pull": {"news": {"_id": {"$in": news_ids}}}}
                        )
                        results.append(result.modified_count > 0)

                        # Si no hay más noticias en el grupo, eliminar el grupo de noticias
                        if result.modified_count > 0:
                            remaining_news = news_collection.find_one({"_id": group_oid}, {"news": 1})
                            if not remaining_news or len(remaining_news.get("news", [])) == 0:
                                news_collection.delete_one({"_id": group_oid})

            # Retornar True si alguna noticia fue eliminada
            return any(results)

        except Exception as e:
            logging.error(f"Error al eliminar noticias: {e}")
            return False
        finally:
            self.client.close()