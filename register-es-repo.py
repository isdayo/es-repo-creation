import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-test-domain-gcixpsleu64xmqjddytna6zmwy.us-west-2.es.amazonaws.com/'
region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository
path = '_snapshot/esdevice'
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "s3-bucket-dev-es-snapshot",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::aws-acct-id:role/es-snapshot",
    "readonly": "true"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)