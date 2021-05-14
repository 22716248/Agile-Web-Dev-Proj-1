import unittest, os
from app import app, db
from app.models import User, Score


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        u1 = User(id=0,username='Test')
        u2 = User(id=1,username='Unit')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # checks password is correct
    def test_password_hashing(self):
        u = User.query.get(0)
        u.setpw('you-will-never-guess')
        self.assertFalse(u.checkpw('dog'))
        self.assertTrue(u.checkpw('you-will-never-guess'))

    # check for no password when user entered a password
    def test_no_password(self):
        u = User.query.get(1)
        self.assertFalse(u.checkpw('you-will-never-guess'))

    if __name__ == '__main__':
        unittest.main(verbosity=2)
