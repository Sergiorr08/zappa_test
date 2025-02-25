import json
def app(event, context):
    print("Se subió un archivo a S3")
    print(event)
    
    # Obtener el nombre del archivo subido
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        print(f"Archivo subido: {object_key} en el bucket: {bucket_name}")
    except KeyError as e:
        print(f"Error al obtener los datos del evento: {e}")
        object_key = "Desconocido"
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Archivo subido: {object_key}')
    }