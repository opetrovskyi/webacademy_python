import boto3, json
from flask import Flask
from StaticClass import StaticFiles


dict = {}
my_bucket_name = 'perfcycle-ip-statistic-html'

app = Flask(__name__)

def all_envs_tags():
    ec2 = boto3.Session(profile_name='webapc').resource('ec2')
    inst = ec2.instances.all()
    all_tags = []
    for instance in inst:
        name = ''
        for tag in instance.tags:
            if tag['Key'] == 'Environment':
                name = tag['Value']
        if name:
            all_tags.append(name)
    return set(all_tags)
environments = all_envs_tags()



ec2 = boto3.Session(profile_name='webapc').resource('ec2')
def get_env(a):
    filters = [{
        'Name': 'tag:Environment',
        'Values': [a]
    }]
    inst = ec2.instances.filter(Filters=filters)
    reply = []
    for instance in inst:
        for tags in instance.tags:
            if tags["Key"] == 'Role':
                role = tags["Value"]
        pip = instance.private_ip_address
        puip = instance.public_ip_address
        reply.append('Role={}, PrivatIP={}, PublicIP={}'.format(role, pip, puip))
    return reply


for i in environments:
    dict[i] = get_env(i)

sess = boto3.Session(profile_name='webapc')
connect = sess.client('s3')

ress =boto3.Session(profile_name='webapc').resource('s3')
connect.create_bucket(Bucket=my_bucket_name)
bucket_policy = ress.BucketPolicy(my_bucket_name)
policy = {
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "Allow Public Access to All Objects",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::perfcycle-ip-statistic-html/*"
  }
  ]
}
website_conf = {
    'ErrorDocument': {
        'Key': 'error.html'
    },
    'IndexDocument': {
        'Suffix': 'index.html'
    }
}

bucket_policy.put(Policy=json.dumps(policy))
bucket_website = ress.BucketWebsite(my_bucket_name)
bucket_website.put(WebsiteConfiguration=website_conf)

try:
    connect.delete_object(Bucket=my_bucket_name, Key='index.html')
except ZeroDivisionError:
    pass
else:
    text = StaticFiles(dict, template_file="templates/index.html").template_env_file()
    connect.put_object(Bucket=my_bucket_name, Key='index.html', Body=text, ContentType='text/html')
    print('created index.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/index.html'.format(my_bucket_name))

def s3_env_files():
    for k, v in dict.items():
        a = StaticFiles(v).template_env_file()
        filename = '{}.html'.format(k)
        connect.put_object(Bucket=my_bucket_name, Key=filename, Body=a, ContentType='text/html')
        print('created {}.html file, url = https://{}.s3-website-us-east-1.amazonaws.com/{}'.format(filename, my_bucket_name, filename))


s3_env_files()


def refresh_s3_env_files():
    global environments
    environments = all_envs_tags()
    s3_env_files()
    return 'Refreshed <br>  <a href="/" title="Go HOME">Go Home</a>'


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
    return refresh_s3_env_files()

