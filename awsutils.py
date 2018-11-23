import keychain
import boto3

AWS_ACCESS_KEY = keychain.get_password('AWS', 'ACCESS_KEY')
AWS_SECRET_KEY = keychain.get_password('AWS', 'SECRET_KEY')

ec2 = boto3.client(
	'ec2', 
	aws_access_key_id=AWS_ACCESS_KEY, 
	aws_secret_access_key=AWS_SECRET_KEY,
	region_name='eu-west-1'
)
response = ec2.describe_instances();

print(response)

