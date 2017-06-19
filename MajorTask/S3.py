import boto3
import json
from AwsMain import *
from AWSec2 import *
from StaticClass import StaticFiles


class AWSs3(AwsMain):
    def __init__(self, profile_name, bucket_name):
        super().__init__(profile_name)
        self.bucket_name = bucket_name
        self.sess = boto3.Session(profile_name=profile_name)
        self.connect = self.sess.client('s3')
        self.ress = boto3.Session(profile_name=profile_name).resource('s3')

    def create_bucket(self):
        self.connect.create_bucket(Bucket=self.bucket_name)

    def bucket_policy(self, policy):
        self.policy = policy
        self.bucket_policy = self.ress.BucketPolicy(self.bucket_name)
        self.bucket_policy.put(Policy=json.dumps(policy))

    def bucket_website(self, website_conf):
        bucket_website = self.ress.BucketWebsite(self.bucket_name)
        bucket_website.put(WebsiteConfiguration=website_conf)

    def delete_index(self):
        self.connect.delete_object(Bucket=self.bucket_name, Key='index.html')


    def upload_index(self, text):
        self.text = text
        self.connect.put_object(Bucket=self.bucket_name, Key='index.html', Body=text, ContentType='text/html')
        print('created index.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/index.html'.format(self.bucket_name))

    def s3_env_files(self, my_dict):
        self.my_dict = my_dict
        for k, v in self.my_dict.items():
            a = StaticFiles(v).template_env_file()
            filename = '{}.html'.format(k)
            self.connect.put_object(Bucket=self.bucket_name, Key=filename, Body=a, ContentType='text/html')
            print('created {}.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/{}'.format(filename, self.bucket_name, filename))

    def refresh_s3_env_files(self):
        ec22 = AWSec2('webapc')
        environments2 = ec22.all_envs_tags()
        my_dict = {}
        for i in environments2:
            my_dict[i] = ec22.get_env(i)
        s33 = AWSs3('webapc', self.bucket_name)
        s33.s3_env_files(my_dict)
        return 'Refreshed <br>  <a href="/" title="Go HOME">Go Home</a>'

    def __repr__(self):
        return str(self)
