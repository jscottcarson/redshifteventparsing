from __future__ import print_function
import json, sys, boto3

# Set up variables
parsed_sns_arn = ''

# Add the event id's you want to alert on from this link to the list below 
# https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html
check_list = ['3000','3519','3520']

## Main body of the code
client = boto3.client('sns')

def lambda_handler(event, context):
    
    #print('Received Event: ' + json.dumps(event, indent=2))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    eventid = message['About this Event']
    
    for item in check_list:
        global result
        search_string = '#REDSHIFT-EVENT-' + str(item)
        if search_string in eventid:
            # For the logs
            print('Found ' + search_string)
            result = 'From SNS: ' + str(eventid)
            
            # Push result to second SNS Topic
            response = client.publish(
                TopicArn=parsed_sns_arn,
                Message='Redshift Event Notification was found' + '\n' + str(result),
                Subject='Parsed Redshift Event ID Notification ')
                
            break
        else:
            result = "No Match Found"
    return(result)







