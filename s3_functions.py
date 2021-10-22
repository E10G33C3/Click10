import boto3
import hashlib
from metodos import obtener_id_usuario, crear_nueva_publicacion
import datetime

# funciones para la conexion con el servicio de alojamiento en la nube S3 de AWS

def upload_file(file_name, bucket, user, descripcion):
    
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
    crear_nueva_publicacion('click10.db', obtener_id_usuario('click10.db', user), ts, f'{object_name}', descripcion)
 
    return response

def show_image(bucket, publicaciones):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in publicaciones:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item[0]}, ExpiresIn = 900)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls