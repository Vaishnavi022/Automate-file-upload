import boto3

s3 = boto3.client('s3')

bucket_name = "associate-file-upload"

s3.upload_file('index.html', bucket_name, 'index.html')

print("✅ File uploaded successfully!")
