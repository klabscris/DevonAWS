import boto3
import logging

#Obtain eferences to AWS services

s3 = boto3.resource('s3')
sns = boto3.resource('sns')

#List bucket names

buffer = ""
for bucket in s3.buckets.all():
    buffer += bucket.name + ", " + bucket.creation_date.strftime ( "%B %d, %Y") + "\n"

print (buffer)

#Publish the bucket name to SNS topics

topic= sns.Topic("arn:aws:sns:us-east-1:844810316301:Test")
response = topic.publish(
    Message= "Mybuckets: \n" + buffer
)

#Read the status code from the response
print (response ['ResponseMetadata'] ['HTTPStatusCode'])

quit