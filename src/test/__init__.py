# import sys
# sys.path.append("D:/Desarrollo web/Proyecto Api rest phyton/API REST NEWS/src/test")

import unittest
from test.TestCreateNewsGoogleDB import TestCreateNewsDB
from test.TestCreateORUpdateUserEndpoint import TestCreateUpdateUserEndpoint
from test.TestCreateORUpdateUserService import TestCreateOrUpdateUserService
from test.TestCreateScheduleDB import TestCreateScheduleDB
from test.TestCreateUserDB import TestCreateUserDB
from test.TestCredencialsValidator import TestCredencialsValidator
from test.TestDBMongoHelper import TestDBmongoHelper
from test.TestDeleteNewsGoogleDB import TestDeleteNewsDB
from test.TestDeleteUserDB import TestDeleteUserDB
from test.TestDeleteUserEndpoint import TestDeleteUserEndpoint
from test.TestDeleteUserService import TestDeleteUserService
from test.TestGetScheduleDB import TestGetScheduleDB
from test.TestGetUserDB import TestGetUserDB
from test.TestGetUserWordsDB import TestGetUserWordsDB
from test.TestGoogleNewsApi import TestGoogleNewsAPI
from test.TestGoogleNewsApiServices import TestGoogleNewsApiService
from test.TestInputCreateorUpdateValidation import TestInputValidator
from test.TestInputDeleteValidation import TestInputDeleteValidator
from test.TestQueryInputValidator import TestQueryValidator
from test.TestScheduleEndpoint import TestScheduleEndpoint
from test.TestScheduleServices import TestScheduleService
from test.TestStopScheduleDB import TestStopScheduleDB
from test.TestUpdateScheduleDB import TestUpdateScheduleDB
from test.TestUpdateUserDB import TestUpdateUserDB


if __name__ == "__main__":
    unittest.main()