from flask import Flask
from Controller import (user_bp)
from Utils import createTabels
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/user")


if __name__ == "__main__":
    load_dotenv()
    createTabels()
    app.run()