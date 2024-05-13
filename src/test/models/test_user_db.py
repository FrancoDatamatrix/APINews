import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("D:/Desarrollo web/Proyecto Api rest phyton/API REST NEWS/src"))))
from src.models.user_db import UserDB

class TestUserDB(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de UserDB para las pruebas
        self.user_db = UserDB(db_url="test_db_url", db_name="test_db_name")
    def test_create_user(self):
        # Configurar datos de prueba para el nuevo usuario
        user_data = {"username": "test_user", "email": "test@example.com"}
        # Simular el resultado de la inserción en la colección de usuarios
        mock_insert_result = MagicMock()
        mock_insert_result.inserted_id = "test_user_id"
        self.user_db.users_collection.insert_one = MagicMock(return_value=mock_insert_result)
        # Llamar al método create_user de UserDB
        user_id = self.user_db.create_user(user_data)
        # Verificar que se haya creado el usuario correctamente y se haya devuelto su ID
        self.assertEqual(user_id, "test_user_id")
    def test_find_user_by_username(self):
        # Configurar datos de prueba para el nombre de usuario a buscar
        username = "test_user"
        # Simular el documento de usuario encontrado en la colección de usuarios
        mock_user_document = {"_id": "test_user_id", "username": "test_user", "email": "test@example.com"}
        self.user_db.users_collection.find_one = MagicMock(return_value=mock_user_document)
        # Llamar al método find_user_by_username de UserDB
        user_document = self.user_db.find_user_by_username(username)
        # Verificar que se haya encontrado el usuario correctamente
        self.assertEqual(user_document, mock_user_document)
    def test_find_users_by_username(self):
        # Configurar datos de prueba para el nombre de usuario a buscar
        username = "test_user"
        # Simular los documentos de usuarios encontrados en la colección de usuarios
        mock_user_documents = [
            {"_id": "user1_id", "username": "test_user", "email": "test1@example.com"},
            {"_id": "user2_id", "username": "test_user", "email": "test2@example.com"}
        ]
        self.user_db.users_collection.find = MagicMock(return_value=mock_user_documents)
        # Llamar al método find_users_by_username de UserDB
        users_documents = self.user_db.find_users_by_username(username)
        # Verificar que se hayan encontrado los usuarios correctamente
        self.assertEqual(users_documents, mock_user_documents)
if __name__ == "__main__":
    unittest.main()
