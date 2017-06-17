#import boto3, json
#from s3_conf import *
#from StaticClass import StaticFiles
#my_bucket_name = 'perfcycle-ip-statistic-html'
#dict = {}
#
#
#sess = boto3.Session(profile_name='webapc')
#connect = sess.client('s3')
#
#ress =boto3.Session(profile_name='webapc').resource('s3')
#connect.create_bucket(Bucket=my_bucket_name)
#bucket_policy = ress.BucketPolicy(my_bucket_name)
#
#
#bucket_policy.put(Policy=json.dumps(policy))
#bucket_website = ress.BucketWebsite(my_bucket_name)
#bucket_website.put(WebsiteConfiguration=website_conf)
#
#try:
#    connect.delete_object(Bucket=my_bucket_name, Key='index.html')
#except ZeroDivisionError:
#    pass
#else:
#    text = StaticFiles(dict, template_file="templates/index.html").template_env_file()
#    connect.put_object(Bucket=my_bucket_name, Key='index.html', Body=text, ContentType='text/html')
#    print('created index.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/index.html'.format(my_bucket_name))
#
#def s3_env_files():
#    for k, v in dict.items():
#        a = StaticFiles(v).template_env_file()
#        filename = '{}.html'.format(k)
#        connect.put_object(Bucket=my_bucket_name, Key=filename, Body=a, ContentType='text/html')
#        print('created {}.html file, url = http://{}.s3-website-us-east-1.amazonaws.com/{}'.format(filename, my_bucket_name, filename))
#
#
#s3_env_files()
