import sys
sys.path.append("D:/Desarrollo web/Proyecto Api rest phyton/API REST NEWS/src/test")

import unittest
from services.test_user_services import TestUsersEndpoint
from models.test_user_db import TestUserDB

if __name__ == "__main__":
    unittest.main()