from flask import Flask
from Controller import (user_bp)
from Utils import createTabels

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/user")


if __name__ == "__main__":
    createTabels()
    app.run()