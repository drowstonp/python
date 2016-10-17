from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 
#db = SQLAlchmey(app)


@app.route('/')
def index():
    return "<body bgcolor='Red'><h1 style='color: white'>Flask!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
