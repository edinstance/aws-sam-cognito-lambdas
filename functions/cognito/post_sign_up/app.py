import os

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

POWERTOOLS_LOG_LEVEL = os.environ.get("POWERTOOLS_LOG_LEVEL", "INFO").upper()

logger = Logger(service="PostSignUp", level=POWERTOOLS_LOG_LEVEL)


@logger.inject_lambda_context
def lambda_handler(event, context: LambdaContext):

    # Perform post sign-up actions here
    # For example, you could send a welcome email or initialize user data

    logger.info("Post sign-up actions started.")
    
    logger.info(f"User confirmed: {event.get('userName', 'unknown')}")
    logger.info(f"Request ID: {context.aws_request_id}")


    logger.info("Post sign-up actions completed successfully.")

    # Return the event to continue the sign-up process
    return event
