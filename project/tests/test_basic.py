import os
import unittest
import sys
# hack to get imports working good
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../')
# sys.path.append('../')
# sys.path.append('databases/')
# print(sys.path)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from main import db, create_app

TEST_DB = 'test.sqlite3'

class BasicTests(unittest.TestCase):
    ## Setup
    # excuted before each test
    def setUp(self):
        # Should do db stuff automatically
        # app = Flask(__name__)
        # db = SQLAlchemy()
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB

        # print(app.config['SQLALCHEMY_DATABASE_URI'])

        self.app = app.test_client()

        # Create the database connection
        db.init_app(app)
        # Load our models into the database
        from databases.user_model import User
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.db = db
        # Load our models into the database
        # from databases.user_model import User
        # with app.app_context():
        #     db.drop_all()
        #     db.create_all()

    # After each test
    def tearDown(self):
        pass

    ## Tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
