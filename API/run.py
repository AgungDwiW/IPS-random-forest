from flask import Flask
from controller import WebApp
import config

app = Flask(__name__)
app.register_blueprint(WebApp)

if __name__ == "__main__":
	app.run()
