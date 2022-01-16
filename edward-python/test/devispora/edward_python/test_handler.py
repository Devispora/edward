
import unittest
import json

from devispora.edward_python import app


class AppTest(unittest.TestCase):
    def test_lambda_handler(self):
        sut = app.lambda_handler('', '')
