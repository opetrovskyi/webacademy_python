from flask import Flask
from StaticClass import StaticFiles
from s3_conf import *
from AWS_main import *
from AWSec2 import *
from S3 import *

dict = {}
my_bucket_name = 'perfcycle-ip-statistic-html'

app = Flask(__name__)
ec2 = AWSec2('webapc')

for i in ec2.all_envs_tags():
    dict[i] = ec2.get_env(i)

a = AWSs3('webapc', my_bucket_name)

a.create_bucket()

a.bucket_policy(policy)

a.bucket_website(website_conf)

a.delete_index()

a.s3_env_files(dict)

text = StaticFiles(dict, template_file="templates/index.html").template_env_file()
a.upload_index(text)


@app.route('/')
def gen_root():
    text1 = StaticFiles(dict, template_file="templates/index.html").template_env_file()
    return text1

@app.route('/<string:env_name>')
def template_environment(env_name):
    envi = env_name.replace('.html', '')
    if envi in dict:
        a1 = StaticFiles(dict[envi]).template_env_file()
        return a1
    else:
        return 'No env found'

@app.route('/refresh')
def refresh():
    __ec2 = AWSs3('webapc', my_bucket_name)
    return __ec2.refresh_s3_env_files()

