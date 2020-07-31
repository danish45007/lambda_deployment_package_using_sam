import json

# ec2Client = boto3.client('ec2')

def lambda_handler(event,context):
    # regRes = ec2Client.describe_regions()
    return {
        # "data": json.dumps({
        #     "regions": regRes["Regions"]
        # })
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }