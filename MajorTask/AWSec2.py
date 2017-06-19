from AwsMain import *
import boto3


class AWSec2(AwsMain):
    def __init__(self, profile_name):
        super().__init__(profile_name)
        self.ec2 = boto3.Session(profile_name=self.profile_name).resource('ec2')
        self.ec2_r = boto3.Session(profile_name='webapc').resource('ec2')

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




