import logging
# import sonrai.platform.aws.arn

def run(ctx):

    iam_client = ctx.get_client().get('iam')
    data = ctx.get_policy_evidence_data()

    logging.info('iam client {}'.format(iam_client))

    # Get policy arn
    # resource_arn = sonrai.platform.aws.arn.parse(data['policyResourceId'])
    policy_arn = data['policyResourceId']


    # https://docs.aws.amazon.com/cli/latest/reference/iam/delete-policy.html
    logging.info('deleting policy: {}'.format(ctx.policy_arn))
    iam_client.delete_policy(PolicyArn=policy_arn)