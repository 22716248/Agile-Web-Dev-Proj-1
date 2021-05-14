import unittest, os
from app import app, db
from app.models import User, Score


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        u1 = User(id=0,username='Test')
        u2 = User(id=1,username='Unit')
        u1.setpw('Hello')
        u2.setpw('World')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # checks password is correct
    def test_password_hashing(self):
        u1 = User.query.get('0')
        u2 = User.query.get('1')
        self.assertFalse(u1.checkpw('dog'))
        self.assertTrue(u1.checkpw('Hello'))
        self.assertFalse(u2.checkpw('cat'))
        self.assertTrue(u2.checkpw('World'))

    # check for no password when user entered a password
    def test_no_password(self):
        u = User.query.get('1')
        self.assertFalse(u.checkpw('Hello'))

    # login returned response is 200 OK
    def test_user_login(self):
        response = self.app.post('/login', data=dict(
            username='Test', email='test@gmail.com', password='Hello'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # login page loads and returned response is 200 OK
    def test_login_page_works(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data) 
        self.assertEqual(response.status_code, 200)

    # login page contains correct infomation/text
    def test_login_page_correct_info(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data)

    # login page contains incorrect infomation/text
    def test_login_page_incorrect_info(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertFalse(b'Hi' in response.data)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
