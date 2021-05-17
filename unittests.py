import unittest, os
from app import app, db
from app.models import User, Score, Question

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        u1 = User(id=0,username='Test')
        u2 = User(id=1,username='Unit')
        u4 = User(id=2,username='Bob')
        u1.setpw('Hello')
        u2.setpw('World')
        q1 = Question(id=0, constellation='Crux')
        q2 = Question(id=1, constellation='Aquarius')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(q1)
        db.session.add(q2)
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
        self.assertFalse(u.checkpw('testing'))

    # checks username is same
    def test_same_username(self):
        u1 = User.query.get('0')
        u2 = User.query.get('1')
        self.assertEqual(u1.username, 'Test')
        self.assertEqual(u2.username, 'Unit')

    # checks username is not the same
    def test_username_is_incorrect(self):
        u1 = User.query.get('0')
        u2 = User.query.get('1')
        self.assertNotEqual(u1.username, 'Test2')
        self.assertNotEqual(u2.username, 'Unit2')

    # test user login works with parameters
    def test_user_login(self):
        u1 = User.query.get('0')
        response = self.app.post('/login', data=dict(
            username = u1.username, password = u1.password_hash), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # login page loads and returned response is 200 OK
    def test_login_page_works(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # login page contains correct infomation/text
    def test_login_page_correct_info(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data)

    # login page contains incorrect infomation/text
    def test_login_page_incorrect_info(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertFalse(b'Welcome' in response.data)

    # register page loads and returned response is 200 OK
    def test_registration_page_works(self):
        response = self.app.get('/register', content_type='html/text') 
        self.assertEqual(response.status_code, 200)

    # register page contains incorrect infomation/text
    def test_registration_page_incorrect_info(self):
        response = self.app.get('/register', content_type='html/text')
        self.assertFalse(b'Welcome' in response.data)

    # register page contains correct infomation/text
    def test_registration_page_correct_info(self):
        response = self.app.get('/register', content_type='html/text')
        self.assertTrue(b'Register' in response.data)

    # test user register page works with parameters
    def test_user_register(self):
        u1 = User.query.get('0')
        response = self.app.post('/register', data=dict(
            username = u1.username, password = u1.password_hash, password_repeat = u1.password_hash), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # test logout works, returns response OK 200
    def test_logout_works(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # index page contains incorrect infomation/text
    def test_index_page_incorrect_info(self):
        response = self.app.get('/index', content_type='html/text')
        self.assertFalse(b'Welcome' in response.data)

    # index page contains correct infomation/text
    def test_index_page_correct_info(self):
        response = self.app.get('/index', content_type='html/text')
        self.assertTrue(b'Constellation' in response.data)
    
    # test index page works, returns response OK 200
    def test_index_works(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # test quiz page works, returns response OK 200
    def test_quiz(self):
        response = self.app.get('/quiz', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # quiz page contains correct infomation/text
    def test_quiz_page_incorrect_info(self):
        response = self.app.get('/quiz', content_type='html/text')
        self.assertFalse(b'Welcome' in response.data)

    # quiz page contains correct infomation/text
    def test_quiz_page_correct_info(self):
        response = self.app.get('/quiz', content_type='html/text')
        self.assertTrue(b'QUIZ' in response.data)

    # quiz works with request parameters
    def test_quiz2(self):
        q = Question.query.get('0')
        response = self.app.post('/quiz', data=dict(
            question = q.id, constellation = 'Crux'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # correct answer to quiz question
    def test_quiz_correct_answer(self):
        q = Question.query.get('0')
        self.assertEqual(q.constellation, 'Crux')
        q1 = Question.query.get('1')
        self.assertEqual(q1.constellation, 'Aquarius')

    if __name__ == '__main__':
        unittest.main(verbosity=2)
