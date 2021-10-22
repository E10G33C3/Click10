import boto3
import hashlib
from metodos import obtener_id_usuario, crear_nueva_publicacion
import datetime


def upload_file(file_name, bucket, user):
    
    # crear nombre cifrado del objeto
    object_name = hashlib.sha256(file_name.encode()).hexdigest() 
    object_name = f"uploads/{object_name}" + file_name[-4:]
    # print(object_name)
    
    #genarar timestamp
    ts = datetime.datetime.now().timestamp()
    
   
    # actualizar nombre de archivo
    file_name = "uploads/"+file_name
    
    #subir archivo a la nube
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    # crear registro de la publicacion en la base de datos
    crear_nueva_publicacion('click10.db', obtener_id_usuario('click10.db', user), ts, f'https://click10.s3.sa-east-1.amazonaws.com/{object_name}')
 
    return response

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls