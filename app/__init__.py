from flask import Flask


app = Flask(__name__)


from app import routes #Import statement is at the bottom to avoid circular imports