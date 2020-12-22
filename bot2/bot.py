import logging

def run(ctx):

    s3 = ctx.get_client().get('s3')

    # Get role name
    resource_id = ctx.resource_id

    splited_resource = resource_id.split(":::")
    bucket_name = splited_resource[1]
    logging.info('Creating bucket: {}-AuditData'.format(bucket_name))
    s3.create_bucket(Bucket="{}-AuditData".format(bucket_name))

    logging.info('Logging bucket: {}-AuditData'.format(bucket_name))
    s3.BucketLogging(Bucket="{}-AuditData".format(bucket_name))
