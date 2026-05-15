from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from routes.api_routes import api

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)