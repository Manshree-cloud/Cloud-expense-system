import json

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))

    expense_id = body.get('expense_id')
    approved = body.get('approved')  # True or False
    manager_id = body.get('manager_id')

    if not expense_id or approved is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid input'})
        }

    # Simulate approval logic
    status = 'approved' if approved else 'rejected'

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Expense {expense_id} has been {status}.',
            'manager_id': manager_id
        })
    }
