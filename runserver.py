# coding=utf8



from flask import Flask, g
from views import login_page
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

app.register_blueprint(login_page)

if __name__ == '__main__':
    app.run()
