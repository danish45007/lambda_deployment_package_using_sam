import json
import boto3
ec2Client = boto3.client('ec2')

def lambda_handler(event,context):
    regRes = ec2Client.describe_regions()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "regions": regRes["Regions"]
        }),
    }