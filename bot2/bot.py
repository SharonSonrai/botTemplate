import logging

def run(ctx):

    s3 = ctx.get_client().get('s3')

    # Get reource id name
    resource_id = ctx.resource_id

    #Get bucket name
    splited_resource = resource_id.split(":::")
    bucket_name = splited_resource[1]
    logging.info('Creating bucket: {}-auditdata'.format(bucket_name))
    s3.create_bucket(Bucket="{}-auditdata".format(bucket_name))


    logging.info('Logging bucket: {}'.format(bucket_name))
    bucket_logging = s3.BucketLogging(Bucket=bucket_name)
    bucket_logging.put(
                    BucketLoggingStatus={
                        'LoggingEnabled': {
                            'TargetBucket': "{}-auditdata".format(bucket_name)
                        }})