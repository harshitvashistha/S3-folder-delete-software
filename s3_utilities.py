import boto3

ACCESS_KEY_ID = 'Insert Here'
SECRET_ACCESS_KEY = 'Insert Here'



client = boto3.client('s3',aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
def is_path_exists(file_path):
  result = client.list_objects(Bucket="cointreau-data-archive", Prefix=file_path )
  exists=False
  if 'Contents' in result:
      exists=True
  return exists
