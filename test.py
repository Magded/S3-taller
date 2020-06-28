import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def download_image(filekey, bucket):
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    s3.download_file(bucket, filekey, f'tmp/{filekey}')

def upload_image(filepath, bucket, save_key):
    try:
        s3.upload_file(filepath, bucket, save_key)
    except ClientError as e:
        print(e)
        return False
    return True

dirname = os.path.dirname(__file__) # Obtiene la base de la ruta
path = os.path.join(dirname, "images/meme.jpg")
upload_image(path, 'macao-taller-test', 'image.jpg')
