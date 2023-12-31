#Header
import boto3
import os

# Set the S3 bucket name and local directory path
s3_bucket_name = 'deladoreen'  # Replace with your S3 bucket name
local_directory = '/home/ssm-user/mys3backup'

def copy_s3_bucket_contents():
    try:
        # Initialize the S3 client with instance profile
        session = boto3.Session()
        s3 = session.client('s3', region_name='us-east-2')

        # Check if the local directory exists, create it if not
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # List objects in the S3 bucket
        objects = s3.list_objects_v2(Bucket=s3_bucket_name)

        # Iterate through S3 objects and copy them to the local directory
        for obj in objects.get('Contents', []):
            s3_object_key = obj['Key']
            local_file_path = os.path.join(local_directory, os.path.basename(s3_object_key))

            # Download the S3 object
            s3.download_file(s3_bucket_name, s3_object_key, local_file_path)
            print('Copied: {} to {}'.format(s3_object_key, local_file_path))

        print('S3 bucket contents copied to the local directory successfully.')

    except Exception as e:
        print('Error: {}'.format(e))

if __name__ == '__main__':
    copy_s3_bucket_contents()
