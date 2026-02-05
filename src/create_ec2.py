import boto3

ec2_client = boto3.client('ec2', region_name='us-east-2')

instance_type = "t2.micro"
ami_id = "ami-03ea746da1a2e36e7"

response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1
)

instance_id = response["Instances"][0]["InstanceId"]

print(response)

print(f"Instância Ec2 id {instance_id} criada com sucesso")