#Using boto3 for creating an ec2 instance with the keypair

#install both awscli and boto3

#create Keypair for the ec2 instance
import boto3
ec2=boto3.resource('ec2')

#Store key-alue pair
outfile = open('ec2-keypair.pem','w')

#create keypair if not exists
key-pair=ec2.create_key_pair(KeyName='ec2-keypair')
keypairout=str(key_pair.key_material)            #Key_material returns the private key
print(keypairout)
outfile.write(keypairout)



#create ec2 instance

import boto3
ec2=boto3.resource('ec2')

#new_instances=ec2.create_instances(
#    ImageId='yourImageID',
#    InstanceType='t2-micro',
#    KeyName='ec2-keypair',
#    Min="min_count of instance",
#    Max="max_count of instance"
#)

new_instances=ec2.create_instances(
    ImageId='ami-0a887e401f7654935',
    InstanceType='t2-micro',
    KeyName='ec2-keypair',
    Min=1,
    Max=5
)

#TO print all instances

for i in new_instances:
	print(new_instances.id,new_instances.instance_type)