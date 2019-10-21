import unittest
from app.models import User
from app import db, create_app

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_default_params(self):
        user0 = User(password='test')
        self.assertTrue(user0.balance == 0)

