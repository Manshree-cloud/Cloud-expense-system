# Cloud-expense-system
# Enterprise Cloud-Based Expense Reimbursement System

## Project Objective  
Design and deploy a secure, scalable, and cloud-native **Expense Reimbursement System** using AWS services.
## Technologies Used  
- AWS Lambda  
- Amazon API Gateway  
- Amazon RDS / DynamoDB  
- Amazon Cognito  
- AWS IAM  
- AWS CloudFormation  
- Amazon CloudWatch  
- Amazon S3  
- Amazon SNS

## Features  
- Secure multi-role login (Employee, Manager, Finance)  
- Expense submission with file upload  
- Approval workflows with notification  
- Real-time logging and metrics  
- Infrastructure as Code (CloudFormation)

## Status  
In Progress — project architecture and backend modules in development.

## Purpose  
This project simulates an enterprise-grade workflow system and is built to demonstrate hands-on system architecture skills, infrastructure automation, and secure AWS cloud-native design practices.
# AWS Expense Reimbursement System

This is a serverless expense reimbursement application demonstrating key AWS cloud concepts including infrastructure as code, Lambda functions, and Cognito authentication.

## Project Structure

- `/infra` - Contains the CloudFormation YAML template that deploys the necessary AWS resources.
- `/lambda` - Contains Lambda function code for submitting and approving expenses (Python).

## Deployment Instructions

1. Deploy the CloudFormation stack from `/infra/cloudformation.yaml` to create AWS resources.
2. Upload Lambda function code (`approve-expense.py`, `submit-expense.py`) to their respective Lambda functions or deploy via CloudFormation.
3. Configure API Gateway (if applicable) and Cognito User Pools for authentication.
4. Test the endpoints.

## Technologies Used

- AWS CloudFormation
- AWS Lambda (Python)
- Amazon Cognito
- Amazon S3
- Python 3.10

---

Feel free to clone and adapt this project for your needs!
