import datetime
import unittest
import json

from devispora.edward_python import app


class AppTest(unittest.TestCase):
    def test_lambda_handler(self):
        print(datetime.datetime.now())
        sut = app.lambda_handler('', '')
        print(datetime.datetime.now())
        # sut = app.lambda_handler('', '')
        # print(datetime.datetime.now())
