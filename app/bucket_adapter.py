from pathlib import Path
import logging
import boto3
from botocore.exceptions import ClientError
import logging
import json
import os

class BucketAdpater:
    def __init__(self, access) -> None:
        """

        Args:
            access (str): Specifie les droit d'accées
        """
        session = boto3.session.Session()

        self.s3_client = session.client(
            service_name="s3",
            aws_access_key_id=os.environ.get(f'S3_{access}_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get(f'S3_{access}_PRIVATE_KEY'),
            endpoint_url=os.environ.get('ENDPOINT'),
            region_name=os.environ.get('REGION'),
        )
        self.bucket_name = os.environ.get('DEFAULT_BUCKET')

    def upload_file(self, path_file: Path, name_file):
        """upload fichier sur ovh

        Args:
            path_file (Path): chemin du fichier à uploader
            name_file (str): nom du fichier à uploader
        """
        try:
            response = self.s3_client.upload_file(
                path_file, self.bucket_name, name_file
            )
        except ClientError as e:
            logging.error(e)
            return False
        return True


    def read_file(self, name_file) -> None:
        """lecture d'un fichier sur ovh

        Args:
            name_file (str): nom du fichier à lire

        Returns:
            json/bool: retourne le contenu du fichier / false si aucun fichier trouvé
        """
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=name_file)
            data = json.loads(response['Body'].read().decode('utf-8'))
            return data
        except ClientError as e:
            logging.error(e)
            return False
