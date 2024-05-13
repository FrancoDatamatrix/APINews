from .DBMongoHelper import DBmongoHelper

class DeleteNewsDB:
    def __init__(self):
     self.db_helper = DBmongoHelper()
     self.news_collection = self.db_helper.get_collection("news")

    def delete_news_by_id(self, news_id):
     result = self.news_collection.delete_one({"id": news_id})
     return result.deleted_count > 0
