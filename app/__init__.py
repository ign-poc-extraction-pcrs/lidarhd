from flask import Flask
from app.controllers import route, api, download_lidar


app = Flask(__name__)

app.register_blueprint(route.route)
app.register_blueprint(api.api)
app.register_blueprint(download_lidar.download_lidar)

