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

my_dict = {}
my_bucket_name = 'perfcycle-ip-statistic-html'