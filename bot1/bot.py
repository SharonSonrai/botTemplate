import logging
import sonrai.platform.aws.arn

def run(ctx):

    iam_client = ctx.get_client().get('iam')

    logging.info('iam client {}'.format(iam_client))
    # Get policy arn
    resource_arn = sonrai.platform.aws.arn.parse(ctx.resource_id)
    policy_arn = resource_arn \
        .assert_service("iam") \
        .assert_type("policy") \
        .resource

    # https://docs.aws.amazon.com/cli/latest/reference/iam/delete-policy.html

    logging.info('deleting policy: {}'.format(ctx.policy_arn))
    iam_client.delete_policy(PolicyArn=policy_arn)