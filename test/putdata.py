import boto3
from faker import Faker
import json

fake = Faker()
client = boto3.client('s3')
lines = []

for i in range(1, 10000):
  line = {
    'id': i, 
    'created': fake.date_time().isoformat(sep=' '), 
    'name': fake.license_plate(), 
    'pcs': fake.random_int()
  }
  lines.append(json.dumps(line))

client.put_object(
  Body='\n'.join(lines),
  Bucket='cdkgluetable-bucket',
  Key='data/20210320120000.json',
)