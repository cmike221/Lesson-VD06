from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'  # Фраза д.б. рандомная

# from app import routes
from app import routes2
