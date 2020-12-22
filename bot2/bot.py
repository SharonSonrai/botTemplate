import logging

def run(ctx):

    s3 = ctx.get_client().get('s3')

    # Get role name
    resource_id = ctx.resource_id

    logging.info('Creating bucket: {}-AuditData'.format(resource_id))
    s3.create_bucket(Bucket="{}-AuditData".format(resource_id))

    logging.info('Logging bucket: {}-AuditData'.format(resource_id))
    s3.BucketLogging(Bucket="{}-AuditData".format(resource_id))
