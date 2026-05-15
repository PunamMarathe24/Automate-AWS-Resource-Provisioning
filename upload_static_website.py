import boto3
import os
import mimetypes

# Create S3 client
s3 = boto3.client('s3')

# Bucket details
bucket_name = 'my-static-site-punam'
region = 'ap-south-1'

# Folder where your website files are stored
website_folder = 'website'

# Upload all files
for root, dirs, files in os.walk(website_folder):
    for file in files:
        file_path = os.path.join(root, file)
        s3_key = os.path.relpath(file_path, website_folder)

        # Detect file type
        content_type, _ = mimetypes.guess_type(file_path)

        # Upload file
        s3.upload_file(
            file_path,
            bucket_name,
            s3_key,
            ExtraArgs={
                'ContentType': content_type or 'application/octet-stream'
            }
        )

print("✅ Upload Complete!")

# Generate website URL
website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"

print("\n🌐 Your Website Link:")
print(website_url)

print("\n👉 Open this in browser:")
print(website_url + "/index.html")
