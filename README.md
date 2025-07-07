# AWS SAM Cognito Lambda Triggers

This repository contains examples on how to use [Cognito Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html) with [AWS Serverless Application Model (SAM)](https://aws.amazon.com/serverless/sam/). It demonstrates implementing a post sign-up Lambda function that gets automatically triggered when a user confirms their registration in a Cognito User Pool.

## Contributing and Questions

If you would like to add anything, ask a question about this or know something that would be helpful to others. Feel free to open a pull request or create an issue.

## More Resources

If you want to learn more here are some resources:

1. I have a repo where this is used in a larger system, which can be found [here](https://github.com/edinstance/AWS-Banking-System).
2. Checkout the SAM GitHub Repository [here](https://github.com/aws/serverless-application-model) or the documentation [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
3. Finally, [here](https://github.com/aws/aws-sam-cli-app-templates) are some examples of using SAM made by AWS.


## Architecture

The project deploys:
- **Cognito User Pool**: Handles user authentication with email verification
- **Cognito User Pool Client**: Allows applications to authenticate users
- **Lambda Function**: Post sign-up trigger that executes after user confirmation
- **CloudWatch Logs**: Centralized logging for the Lambda function

## Prerequisites

- AWS CLI configured with appropriate permissions
- AWS SAM CLI installed
- Python 3.12

## Deployment

1. Build the application:
```bash
sam build
```

2. Deploy to the specific environment on AWS:
```bash
sam deploy --config-env=dev
```

## Cleanup

To remove all resources:
```bash
sam delete --config-env=dev
```