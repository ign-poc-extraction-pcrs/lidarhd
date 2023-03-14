from flask import Blueprint, jsonify
import json
import os
from pathlib import Path
from app.controllers.Config import Config
from app.controllers.download_lidar import PATH_KEY, KEY_JSON_LIDAR
from app.bucket_adapter import BucketAdpater

api = Blueprint('api', __name__, url_prefix='/api')

KEY_JSON_SERVEUR = "host_serveur"
PATH_KEY_SERVEUR = Path(__file__).parent / "../../config_serveur.json"

@api.route('/get/config/key/lidar')
def get_config_lidar():
    # recupere les clé lidar
    statut = "failure"
    key = Config.get_config_json(PATH_KEY, KEY_JSON_LIDAR)
    if key :
        statut = "success"

    return jsonify({"statut": statut, "result": key})

@api.route('/get/config/serveur')
def get_config_serveur():
    # recupere le serveur
    statut = "failure"
    host = os.environ.get('HOST_SERVEUR')
    if host :
        statut = "success"

    return jsonify({"statut": statut, "result": host})


@api.route('/version3/get/dalle', methods=['GET', 'POST'])
def get_dalle_lidar():
    bucketAdpater = BucketAdpater("RO")
    data = bucketAdpater.read_file("file_path_dalle_lidar")

    return jsonify({"result": data})