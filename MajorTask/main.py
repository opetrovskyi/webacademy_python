import boto3, json
from flask import Flask
from StaticClass import StaticFiles
from s3_conf import *


dict = {}
my_bucket_name = 'perfcycle-ip-statistic-html'

app = Flask(__name__)

class AWS:
    def __init__(self, profile_name):
        self.profile_name = profile_name


class AWSec2(AWS):
    def __init__(self, profile_name):
        super().__init__(profile_name)
        self.ec2 = boto3.Session(profile_name=self.profile_name).resource('ec2')
        self.ec2_r = boto3.Session(profile_name='webapc').resource('ec2')
    def all_envs_tags(self):
        inst = self.ec2.instances.all()
        all_tags = []
        for instance in inst:
            name = ''
            for tag in instance.tags:
                if tag['Key'] == 'Environment':
                    name = tag['Value']
            if name:
                all_tags.append(name)
        return set(all_tags)
    def get_env(self, env_name):
        self.env_name = env_name
        filters = [{
            'Name': 'tag:Environment',
            'Values': [env_name]
        }]
        inst = self.ec2_r.instances.filter(Filters=filters)
        reply = []
        for instance in inst:
            for tags in instance.tags:
                if tags["Key"] == 'Role':
                    role = tags["Value"]
            pip = instance.private_ip_address
            puip = instance.public_ip_address
            reply.append('Role={}, PrivatIP={}, PublicIP={}'.format(role, pip, puip))
        return reply


ec2 = AWSec2('webapc')
environments = ec2.all_envs_tags()

for i in environments:
     dict[i] = ec2.get_env(i)

#print(dict)

class AWSs3(AWS):
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
        try:
            self.connect.delete_object(Bucket=self.bucket_name, Key='index.html')
        except ZeroDivisionError:
            pass

    def upload_index(self, text):
        self.text = text
        self.connect.put_object(Bucket=self.bucket_name, Key='index.html', Body=text, ContentType='text/html')
        print('created index.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/index.html'.format(self.bucket_name))

    def s3_env_files(self, dict):
        self.dict = dict
        for k, v in self.dict.items():
            a = StaticFiles(v).template_env_file()
            filename = '{}.html'.format(k)
            self.connect.put_object(Bucket=self.bucket_name, Key=filename, Body=a, ContentType='text/html')
            print('created {}.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/{}'.format(filename, self.bucket_name, filename))

    def refresh_s3_env_files(self):
        ec22 = AWSec2('webapc')
        environments2 = ec22.all_envs_tags()
        dict = {}
        for i in environments2:
            dict[i] = ec22.get_env(i)
        s33 = AWSs3('webapc', self.bucket_name)
        s33.s3_env_files(dict)
        return 'Refreshed <br>  <a href="/" title="Go HOME">Go Home</a>'

    def __repr__(self):
        return str(self)

text = StaticFiles(dict, template_file="templates/index.html").template_env_file()

a = AWSs3('webapc', my_bucket_name)
a.create_bucket()
a.bucket_policy(policy)
a.bucket_website(website_conf)
a.delete_index()
a.upload_index(text)
a.s3_env_files(dict)

a.refresh_s3_env_files()




@app.route('/')
def gen_root():
    text1 = StaticFiles(dict, template_file="templates/index.html").template_env_file()
    return text1
#
#
#
# @app.route('/<string:env_name>')
# def template_environment(env_name):
#     envi = env_name.replace('.html', '')
#     if envi in dict:
#         a1 = StaticFiles(dict[envi]).template_env_file()
#         return a1
#     else:
#         return 'No env found'
#
# @app.route('/refresh')
# def refresh():
#     return refresh_s3_env_files()
#
