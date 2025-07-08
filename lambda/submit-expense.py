import json
import boto3
import os

def lambda_handler(event, context):
    # Placeholder for actual receipt parsing and DB logic
    body = json.loads(event.get('body', '{}'))
    employee_id = body.get('employee_id')
    amount = body.get('amount')
    description = body.get('description')

    # Simulate a response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Expense submitted successfully!',
            'employee_id': employee_id,
            'amount': amount,
            'description': description
        })
    }

